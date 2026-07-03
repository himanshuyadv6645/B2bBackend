import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
from apps.buyers.models import BuyerProfile, BuyerAddress
from apps.sellers.models import SellerProfile
from apps.products.models import Product
from apps.product_variants.models import ProductVariant
from apps.orders.models import Order, OrderItem, SellerOrder
from apps.reviews.models import ProductReview, SellerReview
from apps.categories.models import Category

print("Starting Data Seed for Reviews...")

# Category
category, _ = Category.objects.get_or_create(name='Seed Category', defaults={'description': 'Seed', 'is_active': True})

# Buyer
buyer_user, _ = User.objects.get_or_create(email='buyer_seed@example.com', defaults={'role': 'buyer', 'is_active': True})
if _:
    buyer_user.set_password('password123')
    buyer_user.save()
buyer_profile, _ = BuyerProfile.objects.get_or_create(user=buyer_user, defaults={'first_name': 'Seed', 'last_name': 'Buyer'})

buyer_address, _ = BuyerAddress.objects.get_or_create(
    buyer=buyer_profile,
    defaults={
        'address_type': 'shipping',
        'contact_name': 'Seed Buyer',
        'contact_phone': '9876543210',
        'address_line1': '123 Seed St',
        'city': 'Seed City',
        'state': 'Seed State',
        'pincode': '123456',
        'country': 'India',
        'is_default': True
    }
)

# Seller
seller_user, _ = User.objects.get_or_create(email='seller_seed@example.com', defaults={'role': 'seller', 'is_active': True})
if _:
    seller_user.set_password('password123')
    seller_user.save()
seller_profile, _ = SellerProfile.objects.get_or_create(user=seller_user, defaults={'company_name': 'Seed Seller Inc.', 'status': 'approved'})

import uuid

sku_val = f'SEED-SKU-{uuid.uuid4().hex[:6]}'

# Product
product, _ = Product.objects.get_or_create(
    seller=seller_profile, name='Seeded Product', defaults={'category': category, 'description': 'desc', 'is_active': True, 'sku': sku_val}
)
variant, _ = ProductVariant.objects.get_or_create(product=product, sku='SEED-001', defaults={'price': 100, 'stock': 50})

# Order
order = Order.objects.create(
    buyer=buyer_profile,
    status='delivered',
    total_amount=100,
    shipping_address=buyer_address,
    billing_address=buyer_address
)
seller_order = SellerOrder.objects.create(order=order, seller=seller_profile, status='delivered', subtotal=100)
order_item = OrderItem.objects.create(
    order=order, seller_order=seller_order, seller=seller_profile, variant=variant, quantity=1, unit_price=100, total_price=100
)

# Reviews
ProductReview.objects.create(
    buyer=buyer_profile, order_item=order_item, product=product, variant=variant, seller=seller_profile,
    rating=5, title='Absolutely amazing', comment='This is a pending review for testing the UI.', status='pending', is_verified=True
)

SellerReview.objects.create(
    buyer=buyer_profile, order=order, seller=seller_profile,
    rating=4, title='Good packaging', comment='The packaging was secure. Pending approval test.', status='pending', is_verified=True
)

print("✅ Data seed complete! You should now see pending reviews in the Admin Panel.")
