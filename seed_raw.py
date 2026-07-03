import os
import django
import uuid
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from django.db import connection

print("Starting Raw SQL Data Seed for Reviews...")

with connection.cursor() as cursor:
    # Check if a buyer exists
    cursor.execute("SELECT user_id, id FROM buyer_profiles LIMIT 1")
    buyer = cursor.fetchone()
    if not buyer:
        print("No buyer profile found. Creating a fake buyer user...")
        # Create user
        user_id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO users_user (id, email, password, role, is_active, is_staff, is_superuser, created_at, updated_at) 
            VALUES (%s, 'raw_buyer@test.com', 'pwd', 'buyer', true, false, false, now(), now())
        """, [user_id])
        buyer_profile_id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO buyer_profiles (id, user_id, first_name, last_name, is_verified, created_at, updated_at)
            VALUES (%s, %s, 'Raw', 'Buyer', true, now(), now())
        """, [buyer_profile_id, user_id])
        buyer_id = buyer_profile_id
    else:
        buyer_id = buyer[1]

    # Check if a seller exists
    cursor.execute("SELECT user_id, id FROM seller_profiles WHERE status = 'approved' LIMIT 1")
    seller = cursor.fetchone()
    if not seller:
        print("No seller profile found. Creating a fake seller user...")
        user_id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO users_user (id, email, password, role, is_active, is_staff, is_superuser, created_at, updated_at) 
            VALUES (%s, 'raw_seller@test.com', 'pwd', 'seller', true, false, false, now(), now())
        """, [user_id])
        seller_profile_id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO seller_profiles (id, user_id, company_name, business_type, status, created_at, updated_at)
            VALUES (%s, %s, 'Raw Seller Inc', 'Retail', 'approved', now(), now())
        """, [seller_profile_id, user_id])
        seller_id = seller_profile_id
    else:
        seller_id = seller[1]
    
    # Check if a category exists
    cursor.execute("SELECT id FROM categories LIMIT 1")
    cat = cursor.fetchone()
    if not cat:
        cat_id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO categories (id, name, slug, is_active, created_at, updated_at)
            VALUES (%s, 'Raw Category', 'raw-category', true, now(), now())
        """, [cat_id])
    else:
        cat_id = cat[0]

    # Create Product
    product_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO products (id, seller_id, category_id, name, slug, sku, is_active, is_featured, is_trending, is_top_seller, taxable, is_digital, total_sellers, total_stock, average_rating, total_reviews, views_count, created_at, updated_at, gst, country_of_origin, moq, specifications)
        VALUES (%s, %s, %s, 'Raw Seeded Product', %s, %s, true, false, false, false, true, false, 0, 100, 0, 0, 0, now(), now(), 18.00, 'India', 1, '{}')
    """, [product_id, seller_id, cat_id, f'raw-seeded-product-{str(uuid.uuid4())[:8]}', f'RAW-SKU-{str(uuid.uuid4())[:8]}'])

    # Create Order
    order_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO orders (id, buyer_id, status, total_amount, shipping_address, billing_address, created_at, updated_at)
        VALUES (%s, %s, 'delivered', 150.00, '{"test": "address"}', '{"test": "address"}', now(), now())
    """, [order_id, buyer_id])

    # Create Seller Order
    seller_order_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO seller_orders (id, order_id, seller_id, status, subtotal, created_at, updated_at)
        VALUES (%s, %s, %s, 'delivered', 150.00, now(), now())
    """, [seller_order_id, order_id, seller_id])

    # Create Order Item
    order_item_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO order_items (id, order_id, seller_order_id, seller_id, product_id, quantity, unit_price, total_price, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, 1, 150.00, 150.00, now(), now())
    """, [order_item_id, order_id, seller_order_id, seller_id, product_id])

    # Insert Product Review
    prod_rev_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO product_reviews (id, buyer_id, product_id, seller_id, order_item_id, rating, title, comment, status, is_verified, is_active, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, 5, 'Raw Super Product', 'This is an amazing raw product seeded for UI testing', 'pending', true, true, now(), now())
    """, [prod_rev_id, buyer_id, product_id, seller_id, order_item_id])

    # Insert Seller Review
    sell_rev_id = str(uuid.uuid4())
    cursor.execute("""
        INSERT INTO seller_reviews (id, buyer_id, seller_id, order_id, rating, title, comment, status, is_verified, is_active, created_at, updated_at)
        VALUES (%s, %s, %s, %s, 4, 'Raw Good Seller', 'Seller was fast in shipping', 'pending', true, true, now(), now())
    """, [sell_rev_id, buyer_id, seller_id, order_id])

print("✅ Raw SQL Data seed complete! You should now see pending reviews in the Admin Panel.")
