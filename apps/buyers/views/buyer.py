from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
import urllib.request
import json

from apps.buyers.models import BuyerProfile, BuyerAddress
from apps.buyers.serializers.buyer import BuyerProfileSerializer, BuyerAddressSerializer
from apps.buyers.services import BuyerService
from apps.authentication.models import User
from common.permissions import IsBuyerUser
from common.response import success_response, created_response, not_found_response, bad_request_response


def reverse_geocode_osm(lat, lon):
    """Reverse geocode using OpenStreetMap Nominatim (server-side, no CORS issues)."""
    url = (
        f'https://nominatim.openstreetmap.org/reverse?'
        f'lat={lat}&lon={lon}&format=json&addressdetails=1&accept-language=en'
    )
    req = urllib.request.Request(url, headers={'User-Agent': 'B2BMarketplace/1.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())

    addr = data.get('address', {})
    city = addr.get('city') or addr.get('town') or addr.get('village') or addr.get('county') or ''
    state = addr.get('state') or ''
    pincode = addr.get('postcode') or ''
    country = addr.get('country') or 'India'
    area = addr.get('suburb') or addr.get('neighbourhood') or addr.get('residential') or ''
    road = addr.get('road') or addr.get('pedestrian') or ''

    address_line1 = ''
    if area:
        address_line1 = area
    if road:
        address_line1 = f'{address_line1}, {road}'.strip(', ') if address_line1 else road
    if not address_line1:
        address_line1 = city

    return {
        'city': city,
        'state': state,
        'pincode': pincode,
        'country': country,
        'address_line1': address_line1,
        'address_line2': None,
    }


class BuyerProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    @extend_schema(tags=['Buyers'], summary='Get buyer profile')
    def get(self, request, *args, **kwargs):
        profile = BuyerService.get_profile(request.user)
        if not profile:
            return not_found_response('Profile not found')
        serializer = BuyerProfileSerializer(profile)
        return success_response(data=serializer.data)

    @extend_schema(tags=['Buyers'], summary='Update buyer profile')
    def patch(self, request, *args, **kwargs):
        profile = BuyerService.update_profile(request.user, request.data)
        serializer = BuyerProfileSerializer(profile)
        return success_response(data=serializer.data, message='Profile updated')


class BuyerAddressListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]

    def get_queryset(self):
        profile = BuyerService.get_profile(self.request.user)
        if not profile:
            return BuyerAddress.objects.none()
        return BuyerService.get_addresses(profile)

    def get_serializer_class(self):
        return BuyerAddressSerializer

    @extend_schema(tags=['Buyers'], summary='List buyer addresses')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Buyers'], summary='Create buyer address')
    def post(self, request, *args, **kwargs):
        profile = BuyerService.get_profile(request.user)
        if not profile:
            return not_found_response('Complete your profile first')

        serializer = BuyerAddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address = BuyerService.create_address(profile, serializer.validated_data)
        return created_response(data=BuyerAddressSerializer(address).data, message='Address created')


class BuyerAddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsBuyerUser]
    serializer_class = BuyerAddressSerializer

    def get_object(self):
        profile = BuyerService.get_profile(self.request.user)
        return BuyerAddress.objects.get(id=self.kwargs['pk'], buyer=profile)

    @extend_schema(tags=['Buyers'], summary='Get address details')
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=['Buyers'], summary='Update address')
    def patch(self, request, *args, **kwargs):
        address = self.get_object()
        address = BuyerService.update_address(address, request.data)
        return success_response(data=BuyerAddressSerializer(address).data, message='Address updated')

    @extend_schema(tags=['Buyers'], summary='Delete address')
    def delete(self, request, *args, **kwargs):
        profile = BuyerService.get_profile(request.user)
        BuyerService.delete_address(self.kwargs['pk'], profile)
        return success_response(message='Address deleted')


class SaveDetectedLocationView(APIView):
    """Save auto-detected browser location as the user's default delivery address."""
    permission_classes = [IsAuthenticated, IsBuyerUser]

    @extend_schema(
        tags=['Buyers'],
        summary='Save detected location',
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'latitude': {'type': 'number'},
                    'longitude': {'type': 'number'},
                    'city': {'type': 'string'},
                    'state': {'type': 'string'},
                    'pincode': {'type': 'string'},
                    'country': {'type': 'string'},
                    'address_line1': {'type': 'string'},
                    'address_line2': {'type': 'string'},
                    'contact_name': {'type': 'string'},
                    'contact_phone': {'type': 'string'},
                },
                'required': ['latitude', 'longitude'],
            }
        },
    )
    def post(self, request):
        profile = BuyerService.get_profile(request.user)
        if not profile:
            return not_found_response('Complete your profile first')

        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        if not latitude or not longitude:
            return bad_request_response('latitude and longitude are required')

        city = request.data.get('city', '')
        state = request.data.get('state', '')
        pincode = request.data.get('pincode', '')
        country = request.data.get('country', 'India')
        address_line1 = request.data.get('address_line1', '')
        address_line2 = request.data.get('address_line2', '')

        # Server-side reverse geocoding if fields not provided
        if not city or not state or not pincode:
            try:
                geo = reverse_geocode_osm(latitude, longitude)
                city = city or geo['city']
                state = state or geo['state']
                pincode = pincode or geo['pincode']
                country = country or geo['country']
                address_line1 = address_line1 or geo['address_line1']
                address_line2 = address_line2 or geo['address_line2']
            except Exception:
                if not all([city, state, pincode]):
                    return bad_request_response('Could not determine location. Please provide city, state, and pincode.')

        contact_name = request.data.get('contact_name', '') or profile.full_name
        contact_phone = request.data.get('contact_phone', '') or (profile.phone or '')

        existing = profile.addresses.filter(
            latitude=latitude, longitude=longitude
        ).first()

        if existing:
            address = BuyerService.update_address(existing, {
                'city': city,
                'state': state,
                'pincode': pincode,
                'country': country,
                'address_line1': address_line1 or existing.address_line1,
                'address_line2': address_line2 or existing.address_line2,
                'latitude': latitude,
                'longitude': longitude,
            })
            return success_response(data=BuyerAddressSerializer(address).data, message='Location updated')

        default_shipping = profile.addresses.filter(
            address_type='shipping', is_default=True
        ).first()

        address_data = {
            'address_type': 'shipping',
            'label': 'Detected Location',
            'contact_name': contact_name,
            'contact_phone': contact_phone or '0000000000',
            'address_line1': address_line1 or f'{city}, {state}',
            'address_line2': address_line2,
            'city': city,
            'state': state,
            'pincode': pincode,
            'country': country,
            'latitude': latitude,
            'longitude': longitude,
            'is_default': not default_shipping,
        }

        address = BuyerService.create_address(profile, address_data)
        return created_response(data=BuyerAddressSerializer(address).data, message='Location saved')
