from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'buyer':
            from apps.buyers.models import BuyerProfile
            BuyerProfile.objects.create(
                user=instance,
                first_name='',
                last_name='',
            )
        elif instance.role == 'seller':
            from apps.sellers.models import SellerProfile
            SellerProfile.objects.create(
                user=instance,
                company_name=instance.email.split('@')[0],
                gstin=None,
                pan_number=None,
                contact_name='',
                contact_phone='',
            )
