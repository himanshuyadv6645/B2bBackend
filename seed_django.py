import os
import django
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from django.contrib.auth import get_user_model
from apps.buyers.models import BuyerProfile, BuyerAddress
from apps.sellers.models import SellerProfile
from apps.products.models import Product
from apps.product_variants.models import ProductVariant
from apps.categories.models import Category
from apps.orders.models import Order, SellerOrder, OrderItem
from apps.reviews.models import ProductReview, SellerReview

User = get_user_model()

print("Starting seed...")

# 1. Buyer User + Profile + Address
buyer_user, created = User.objects.get_or_create(
    email='seedbuyer@test.com',
    defaults={'role': 'buyer', 'is_active': True}
)
if created:
    buyer_user.set_password('password123')
    buyer_user.save()

buyer_profile, _ = BuyerProfile.objects.get_or_create(
    user=buyer_user,
    defaults={'first_name': 'Seed', 'last_name': 'Buyer'}
)

buyer_address, _ = BuyerAddress.objects.get_or_create(
    buyer=buyer_profile,
    address_type='shipping',
    defaults={
        'contact_name': 'Seed Buyer',
        'contact_phone': '9876543210',
        'address_line1': '123 Test Street',
        'city': 'Mumbai',
        'state': 'Maharashtra',
        'pincode': '400001',
        'country': 'India',
        'is_default': True,
    }
)

# 2. Seller User + Profile
seller_user, created = User.objects.get_or_create(
    email='seedseller@test.com',
    defaults={'role': 'seller', 'is_active': True}
)
if created:
    seller_user.set_password('password123')
    seller_user.save()

seller_profile, _ = SellerProfile.objects.get_or_create(
    user=seller_user,
    defaults={'company_name': 'Seed Seller Pvt Ltd', 'status': 'approved'}
)

# 3. Category
category, _ = Category.objects.get_or_create(
    name='Seed Category',
    defaults={'slug': f'seed-category-{uuid.uuid4().hex[:6]}', 'is_active': True}
)

# 4. Product
product, _ = Product.objects.get_or_create(
    name='Seed Test Product',
    seller=seller_profile,
    defaults={
        'category': category,
        'sku': f'SEED-{uuid.uuid4().hex[:8]}',
        'description': 'A seeded product for testing reviews',
        'retail_price': 500,
        'min_selling_price': 400,
        'is_active': True,
    }
)

# 5. ProductVariant
variant, _ = ProductVariant.objects.get_or_create(
    product=product,
    name='Default Variant',
    defaults={
        'sku': f'SEED-VAR-{uuid.uuid4().hex[:8]}',
        'sort_order': 0,
        'total_sellers': 1,
        'total_stock': 100,
    }
)

# 6. Order (all required NOT NULL fields filled)
order = Order.objects.create(
    order_number=f'ORD-SEED-{uuid.uuid4().hex[:8]}',
    buyer=buyer_profile,
    status='delivered',
    payment_status='paid',
    billing_address=buyer_address,
    shipping_address=buyer_address,
    subtotal=400.00,
    total_tax=72.00,
    total_shipping=0.00,
    total_discount=0.00,
    total_amount=472.00,
)

# 7. SellerOrder
seller_order = SellerOrder.objects.create(
    order=order,
    seller=seller_profile,
    status='delivered',
    subtotal=400.00,
    total_tax=72.00,
    total_shipping=0.00,
    total_amount=472.00,
)

# 8. OrderItem
order_item = OrderItem.objects.create(
    order=order,
    seller=seller_profile,
    variant=variant,
    product_name=product.name,
    variant_name=variant.name,
    quantity=1,
    unit_price=400.00,
    tax_rate=18.00,
    tax_amount=72.00,
    shipping_charge=0.00,
    discount=0.00,
    total_price=472.00,
    status='delivered',
)

# 9. Product Reviews (pending)
reviews_data = [
    {'rating': 5, 'title': 'Excellent Product!', 'comment': 'Really loved this product. Quality is top-notch and delivery was super fast.'},
    {'rating': 4, 'title': 'Very Good', 'comment': 'Product is great, minor packaging issue but overall satisfied.'},
    {'rating': 3, 'title': 'Decent Quality', 'comment': 'Average product, nothing special but does the job.'},
]

for i, rd in enumerate(reviews_data):
    # Need unique order_item for each review (unique_together = buyer + order_item)
    if i > 0:
        oi = OrderItem.objects.create(
            order=order, seller=seller_profile, variant=variant,
            product_name=product.name, variant_name=variant.name,
            quantity=1, unit_price=400.00, tax_rate=18.00, tax_amount=72.00,
            shipping_charge=0.00, discount=0.00, total_price=472.00, status='delivered',
        )
    else:
        oi = order_item

    ProductReview.objects.create(
        buyer=buyer_profile,
        product=product,
        variant=variant,
        seller=seller_profile,
        order_item=oi,
        rating=rd['rating'],
        title=rd['title'],
        comment=rd['comment'],
        status='pending',
        is_verified=True,
        is_active=True,
    )
    print(f"  [OK] Created product review: {rd['title']}")

# 10. Seller Reviews (pending) - need unique order per review (unique_together = buyer + order)
seller_reviews_data = [
    {'rating': 5, 'title': 'Best Seller!', 'comment': 'Very professional and fast delivery. Highly recommend.'},
    {'rating': 4, 'title': 'Good Experience', 'comment': 'Seller was responsive and product was as described.'},
]

for i, srd in enumerate(seller_reviews_data):
    if i > 0:
        extra_order = Order.objects.create(
            order_number=f'ORD-SEED-{uuid.uuid4().hex[:8]}',
            buyer=buyer_profile, status='delivered', payment_status='paid',
            billing_address=buyer_address, shipping_address=buyer_address,
            subtotal=400.00, total_tax=72.00, total_shipping=0.00,
            total_discount=0.00, total_amount=472.00,
        )
    else:
        extra_order = order

    SellerReview.objects.create(
        buyer=buyer_profile,
        seller=seller_profile,
        order=extra_order,
        rating=srd['rating'],
        title=srd['title'],
        comment=srd['comment'],
        status='pending',
        is_verified=True,
        is_active=True,
    )
    print(f"  [OK] Created seller review: {srd['title']}")

print("\nSeed complete! 3 product reviews + 2 seller reviews created with 'pending' status.")
print("Go to Admin Panel -> Reviews to see them.")
