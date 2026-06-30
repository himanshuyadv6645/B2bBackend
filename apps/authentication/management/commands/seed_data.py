import random
import uuid
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify
from datetime import timedelta

from apps.authentication.models import User
from apps.buyers.models import BuyerProfile, BuyerAddress
from apps.sellers.models import SellerProfile, SellerWarehouse
from apps.categories.models import Category
from apps.brands.models import Brand
from apps.products.models import Product, ProductAttribute, ProductImage
from apps.product_variants.models import ProductVariant, VariantAttribute, VariantImage
from apps.pricing.models import SellerPricing, WholesaleTier
from apps.inventory.models import Inventory, StockHistory
from apps.cart.models import Cart, CartItem
from apps.orders.models import Order, OrderItem, SellerOrder, Invoice
from apps.reviews.models import ProductReview, SellerReview
from apps.notifications.models import Notification


# ============================================================
# FREE STOCK IMAGES (Unsplash / Picsum)
# ============================================================

PRODUCT_IMAGES = {
    'dell-latitude-5540': [
        'https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=600',
        'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=600',
    ],
    'hp-probook-450': [
        'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600',
        'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600',
    ],
    'lenovo-thinkpad-x1': [
        'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=600',
        'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600',
    ],
    'macbook-air-m3': [
        'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600',
        'https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=600',
    ],
    'samsung-galaxy-s24': [
        'https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=600',
        'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600',
    ],
    'iphone-15-pro': [
        'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600',
        'https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?w=600',
    ],
    'cisco-router': [
        'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600',
        'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600',
    ],
    'tp-link-switch': [
        'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600',
        'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600',
    ],
    'sony-headphones': [
        'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600',
        'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=600',
    ],
    'jbl-speaker': [
        'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=600',
        'https://images.unsplash.com/photo-1545454675-3531b543be5d?w=600',
    ],
    'hikvision-cctv': [
        'https://images.unsplash.com/photo-1557597774-9d273605dfa9?w=600',
        'https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=600',
    ],
    'samsung-ssd': [
        'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=600',
        'https://images.unsplash.com/photo-1597858520171-563a8e8b9925?w=600',
    ],
    'hp-printer': [
        'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=600',
        'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600',
    ],
    'apc-ups': [
        'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600',
    ],
    'logitech-mouse': [
        'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=600',
        'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=600',
    ],
}

SELLER_LOGOS = [
    'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=200',
    'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=200',
    'https://images.unsplash.com/photo-1560472355-536de3962603?w=200',
]

CATEGORY_ICONS = {
    'laptops': '💻',
    'mobiles': '📱',
    'networking': '🌐',
    'audio': '🎧',
    'security': '🔒',
    'storage': '💾',
    'printers': '🖨️',
    'industrial': '⚙️',
    'accessories': '🖱️',
    'power': '🔋',
}

USER_AVATARS = [
    'https://i.pravatar.cc/150?img=1',
    'https://i.pravatar.cc/150?img=2',
    'https://i.pravatar.cc/150?img=3',
    'https://i.pravatar.cc/150?img=4',
    'https://i.pravatar.cc/150?img=5',
    'https://i.pravatar.cc/150?img=6',
    'https://i.pravatar.cc/150?img=7',
    'https://i.pravatar.cc/150?img=8',
]


class Command(BaseCommand):
    help = 'Seed the database with demo data for all panels'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear existing data before seeding')

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            self._clear_data()

        self.stdout.write(self.style.SUCCESS('Starting seed...'))

        self._create_users()
        self._create_categories()
        self._create_brands()
        self._create_products()
        self._create_seller_data()
        self._create_inventory()
        self._create_cart_data()
        self._create_orders()
        self._create_reviews()
        self._create_notifications()

        self.stdout.write(self.style.SUCCESS('\n[DONE] Seed completed successfully!'))
        self._print_summary()

    def _clear_data(self):
        Notification.objects.all().delete()
        SellerReview.objects.all().delete()
        ProductReview.objects.all().delete()
        Invoice.objects.all().delete()
        SellerOrder.objects.all().delete()
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        CartItem.objects.all().delete()
        Cart.objects.all().delete()
        StockHistory.objects.all().delete()
        Inventory.objects.all().delete()
        WholesaleTier.objects.all().delete()
        SellerPricing.objects.all().delete()
        VariantImage.objects.all().delete()
        VariantAttribute.objects.all().delete()
        ProductVariant.all_objects.all().delete()
        ProductImage.objects.all().delete()
        ProductAttribute.objects.all().delete()
        Product.all_objects.all().delete()
        Brand.objects.all().delete()
        Category.objects.all().delete()
        SellerWarehouse.objects.all().delete()
        SellerProfile.objects.all().delete()
        BuyerAddress.objects.all().delete()
        BuyerProfile.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        self.stdout.write('  Cleared all data.')

    def _create_users(self):
        self.stdout.write('\n1. Creating users...')

        # Admin (already exists, skip)
        self.admin = User.objects.filter(role='admin').first()

        # Buyers
        buyers_data = [
            {'email': 'ravi@buyer.com', 'first_name': 'Ravi', 'last_name': 'Kumar', 'phone': '9876543210', 'company': 'Ravi Enterprises', 'business_type': 'Retailer', 'city': 'Mumbai', 'state': 'Maharashtra'},
            {'email': 'priya@buyer.com', 'first_name': 'Priya', 'last_name': 'Sharma', 'phone': '9876543211', 'company': 'Sharma Traders', 'business_type': 'Distributor', 'city': 'Delhi', 'state': 'Delhi'},
            {'email': 'amit@buyer.com', 'first_name': 'Amit', 'last_name': 'Patel', 'phone': '9876543212', 'company': 'Patel Electronics', 'business_type': 'Wholesaler', 'city': 'Ahmedabad', 'state': 'Gujarat'},
            {'email': 'neha@buyer.com', 'first_name': 'Neha', 'last_name': 'Gupta', 'phone': '9876543213', 'company': 'Gupta Solutions', 'business_type': 'Retailer', 'city': 'Bangalore', 'state': 'Karnataka'},
            {'email': 'vikram@buyer.com', 'first_name': 'Vikram', 'last_name': 'Singh', 'phone': '9876543214', 'company': 'Singh Mart', 'business_type': 'Retailer', 'city': 'Jaipur', 'state': 'Rajasthan'},
            {'email': 'anjali@buyer.com', 'first_name': 'Anjali', 'last_name': 'Reddy', 'phone': '9876543215', 'company': 'Reddy Computers', 'business_type': 'Dealer', 'city': 'Hyderabad', 'state': 'Telangana'},
        ]

        self.buyers = []
        for bd in buyers_data:
            user = User.objects.create_user(
                email=bd['email'],
                password='buyer123',
                role='buyer',
                phone=bd['phone'],
                is_email_verified=True,
            )
            # Signal auto-creates profile, so get and update it
            profile = user.buyer_profile
            profile.first_name = bd['first_name']
            profile.last_name = bd['last_name']
            profile.phone = bd['phone']
            profile.company_name = bd['company']
            profile.business_type = bd['business_type']
            profile.avatar = random.choice(USER_AVATARS)
            profile.is_verified = True
            profile.save()

            # Create address
            addr = BuyerAddress.objects.filter(buyer=profile, address_type='shipping').first()
            if not addr:
                addr = BuyerAddress(buyer=profile, address_type='shipping')
            addr.label = 'Office'
            addr.contact_name = f'{bd["first_name"]} {bd["last_name"]}'
            addr.contact_phone = bd['phone']
            addr.address_line1 = f'123, {bd["city"]} Industrial Area'
            addr.address_line2 = 'Near Main Road'
            addr.city = bd['city']
            addr.state = bd['state']
            addr.pincode = '400001'
            addr.is_default = True
            addr.save()

            # Billing address
            addr2 = BuyerAddress.objects.filter(buyer=profile, address_type='billing').first()
            if not addr2:
                addr2 = BuyerAddress(buyer=profile, address_type='billing')
            addr2.label = 'Billing'
            addr2.contact_name = f'{bd["first_name"]} {bd["last_name"]}'
            addr2.contact_phone = bd['phone']
            addr2.address_line1 = f'456, {bd["city"]} Business Park'
            addr2.city = bd['city']
            addr2.state = bd['state']
            addr2.pincode = '400001'
            addr2.is_default = True
            addr2.save()

            Cart.objects.get_or_create(buyer=profile)
            self.buyers.append(profile)
            self.stdout.write(f'  [OK] Buyer: {bd["email"]} (password: buyer123)')

        # Sellers
        sellers_data = [
            {'email': 'techhub@seller.com', 'company': 'TechHub Electronics', 'contact': 'Rajesh Mehta', 'phone': '9876543220', 'city': 'Mumbai', 'state': 'Maharashtra', 'desc': 'Leading electronics distributor since 2010. Authorized dealer for Dell, HP, Lenovo.'},
            {'email': 'digital@seller.com', 'company': 'Digital World', 'contact': 'Sanjay Kumar', 'phone': '9876543221', 'city': 'Delhi', 'state': 'Delhi', 'desc': 'One-stop shop for all IT and networking equipment. Competitive wholesale prices.'},
            {'email': 'circuit@seller.com', 'company': 'Circuit Masters', 'contact': 'Anand Joshi', 'phone': '9876543222', 'city': 'Pune', 'state': 'Maharashtra', 'desc': 'Specialized in industrial electronics, security systems, and surveillance equipment.'},
        ]

        self.sellers = []
        for sd in sellers_data:
            user = User.objects.create_user(
                email=sd['email'],
                password='seller123',
                role='seller',
                phone=sd['phone'],
                is_email_verified=True,
            )
            # Signal auto-creates profile, so get and update it
            profile = user.seller_profile
            profile.company_name = sd['company']
            profile.gstin = f'27AAAAA{random.randint(1000,9999)}A1Z5'
            profile.pan_number = f'ABCDE{random.randint(1000,9999)}F'
            profile.contact_name = sd['contact']
            profile.contact_phone = sd['phone']
            profile.description = sd['desc']
            profile.business_type = 'Distributor'
            profile.status = 'approved'
            profile.approval_date = timezone.now()
            profile.is_verified = True
            profile.commission_rate = Decimal('2.50')
            profile.rating = Decimal(str(round(random.uniform(4.0, 4.9), 2)))
            profile.total_ratings = random.randint(50, 500)
            profile.logo = random.choice(SELLER_LOGOS)
            profile.save()

            warehouse = SellerWarehouse.objects.filter(seller=profile, is_primary=True).first()
            if not warehouse:
                warehouse = SellerWarehouse(seller=profile, is_primary=True)
            warehouse.name = f'{sd["company"]} Main Warehouse'
            warehouse.contact_phone = sd['phone']
            warehouse.address_line1 = f'789, {sd["city"]} Industrial Estate'
            warehouse.city = sd['city']
            warehouse.state = sd['state']
            warehouse.pincode = '400001'
            warehouse.is_active = True
            warehouse.save()

            self.sellers.append({'profile': profile, 'warehouse': warehouse})
            self.stdout.write(f'  [OK] Seller: {sd["email"]} (password: seller123)')

    def _create_categories(self):
        self.stdout.write('\n2. Creating categories...')

        categories_data = {
            'Electronics': {
                'icon': '📱',
                'children': {
                    'Laptops & Computers': {'icon': '💻'},
                    'Mobile & Accessories': {'icon': '📱'},
                    'Networking Equipment': {'icon': '🌐'},
                    'Audio & Video': {'icon': '🎧'},
                    'Security Systems': {'icon': '🔒'},
                    'Storage & Memory': {'icon': '💾'},
                    'Printers & Scanners': {'icon': '🖨️'},
                    'Power & UPS': {'icon': '🔋'},
                    'Computer Accessories': {'icon': '🖱️'},
                }
            }
        }

        self.categories = {}
        for cat_name, cat_data in categories_data.items():
            parent = Category.objects.create(
                name=cat_name,
                description=f'All {cat_name} products',
                icon=cat_data['icon'],
                is_active=True,
                meta_title=cat_name,
            )
            self.categories[cat_name] = parent
            self.stdout.write(f'  [OK] {cat_name}')

            for child_name, child_data in cat_data['children'].items():
                child = Category.objects.create(
                    parent=parent,
                    name=child_name,
                    description=f'Best {child_name} at wholesale prices',
                    icon=child_data['icon'],
                    is_active=True,
                    meta_title=child_name,
                )
                self.categories[child_name] = child
                self.stdout.write(f'    -- {child_name}')

    def _create_brands(self):
        self.stdout.write('\n3. Creating brands...')

        brands_data = [
            {'name': 'Dell', 'desc': 'American multinational computer technology company', 'featured': True},
            {'name': 'HP', 'desc': 'Hewlett-Packard - Leading technology company', 'featured': True},
            {'name': 'Lenovo', 'desc': 'Chinese multinational technology company', 'featured': True},
            {'name': 'Apple', 'desc': 'American multinational technology company', 'featured': True},
            {'name': 'Samsung', 'desc': 'South Korean multinational electronics company', 'featured': True},
            {'name': 'Cisco', 'desc': 'American multinational technology conglomerate', 'featured': True},
            {'name': 'TP-Link', 'desc': 'Chinese networking equipment manufacturer', 'featured': False},
            {'name': 'Sony', 'desc': 'Japanese multinational conglomerate', 'featured': True},
            {'name': 'JBL', 'desc': 'American audio electronics company', 'featured': False},
            {'name': 'Hikvision', 'desc': 'Chinese state-owned manufacturer of video surveillance equipment', 'featured': False},
            {'name': 'Logitech', 'desc': 'Swiss computer peripherals manufacturer', 'featured': False},
            {'name': 'APC', 'desc': 'American manufacturer of uninterruptible power supplies', 'featured': False},
        ]

        self.brands = {}
        for bd in brands_data:
            brand = Brand.objects.create(
                name=bd['name'],
                description=bd['desc'],
                is_active=True,
                is_featured=bd['featured'],
            )
            self.brands[bd['name']] = brand
            self.stdout.write(f'  [OK] {bd["name"]}')

    def _create_products(self):
        self.stdout.write('\n4. Creating products...')

        products_data = [
            # Laptops
            {
                'name': 'Dell Latitude 5540 Business Laptop',
                'category': 'Laptops & Computers',
                'brand': 'Dell',
                'sku': 'DELL-LAT-5540',
                'hsn': '8471',
                'desc': '15.6-inch FHD display, Intel Core i7-1365U, 16GB RAM, 512GB SSD, Windows 11 Pro. Perfect for business professionals who need reliable performance.',
                'short_desc': '15.6" FHD | i7-1365U | 16GB | 512GB SSD',
                'image_key': 'dell-latitude-5540',
                'price': Decimal('72999'),
                'attrs': [
                    ('Display', '15.6 inch FHD'),
                    ('Processor', 'Intel Core i7-1365U'),
                    ('RAM', '16GB DDR4'),
                    ('Storage', '512GB NVMe SSD'),
                    ('OS', 'Windows 11 Pro'),
                    ('Weight', '1.76 kg'),
                ],
                'variants': [
                    ('16GB/512GB', 'DELL-LAT-5540-16', Decimal('72999')),
                    ('32GB/1TB', 'DELL-LAT-5540-32', Decimal('92999')),
                ],
            },
            {
                'name': 'HP ProBook 450 G10 Laptop',
                'category': 'Laptops & Computers',
                'brand': 'HP',
                'sku': 'HP-PB-450G10',
                'hsn': '8471',
                'desc': '15.6-inch Full HD display, Intel Core i5-1335U, 8GB RAM, 512GB SSD. Built for productivity with security features.',
                'short_desc': '15.6" FHD | i5-1335U | 8GB | 512GB SSD',
                'image_key': 'hp-probook-450',
                'price': Decimal('54999'),
                'attrs': [
                    ('Display', '15.6 inch FHD'),
                    ('Processor', 'Intel Core i5-1335U'),
                    ('RAM', '8GB DDR4'),
                    ('Storage', '512GB NVMe SSD'),
                    ('OS', 'Windows 11 Home'),
                ],
                'variants': [
                    ('8GB/512GB', 'HP-PB-450-8', Decimal('54999')),
                    ('16GB/512GB', 'HP-PB-450-16', Decimal('64999')),
                ],
            },
            {
                'name': 'Lenovo ThinkPad X1 Carbon Gen 11',
                'category': 'Laptops & Computers',
                'brand': 'Lenovo',
                'sku': 'LEN-X1C-G11',
                'hsn': '8471',
                'desc': '14-inch 2.8K OLED display, Intel Core i7-1365U, 16GB RAM, 512GB SSD. Ultra-lightweight business laptop.',
                'short_desc': '14" 2.8K OLED | i7 | 16GB | 512GB SSD',
                'image_key': 'lenovo-thinkpad-x1',
                'price': Decimal('124999'),
                'attrs': [
                    ('Display', '14 inch 2.8K OLED'),
                    ('Processor', 'Intel Core i7-1365U'),
                    ('RAM', '16GB LPDDR5'),
                    ('Storage', '512GB Gen4 SSD'),
                    ('Weight', '1.12 kg'),
                ],
                'variants': [
                    ('16GB/512GB', 'LEN-X1C-16', Decimal('124999')),
                    ('32GB/1TB', 'LEN-X1C-32', Decimal('164999')),
                ],
            },
            {
                'name': 'Apple MacBook Air M3 15-inch',
                'category': 'Laptops & Computers',
                'brand': 'Apple',
                'sku': 'APL-MBA-M3-15',
                'hsn': '8471',
                'desc': '15.3-inch Liquid Retina display, Apple M3 chip, 8GB RAM, 256GB SSD. Impossibly thin with incredible performance.',
                'short_desc': '15.3" Retina | M3 | 8GB | 256GB SSD',
                'image_key': 'macbook-air-m3',
                'price': Decimal('144900'),
                'attrs': [
                    ('Display', '15.3 inch Liquid Retina'),
                    ('Processor', 'Apple M3'),
                    ('RAM', '8GB Unified'),
                    ('Storage', '256GB SSD'),
                    ('OS', 'macOS Sonoma'),
                    ('Weight', '1.51 kg'),
                ],
                'variants': [
                    ('8GB/256GB', 'APL-MBA-M3-8', Decimal('144900')),
                    ('16GB/512GB', 'APL-MBA-M3-16', Decimal('174900')),
                ],
            },
            # Mobiles
            {
                'name': 'Samsung Galaxy S24 Ultra',
                'category': 'Mobile & Accessories',
                'brand': 'Samsung',
                'sku': 'SAM-S24U-256',
                'hsn': '8517',
                'desc': '6.8-inch Dynamic AMOLED 2X, Snapdragon 8 Gen 3, 12GB RAM, 256GB storage. AI-powered smartphone with S Pen.',
                'short_desc': '6.8" AMOLED | SD 8 Gen 3 | 12GB | 256GB',
                'image_key': 'samsung-galaxy-s24',
                'price': Decimal('129999'),
                'attrs': [
                    ('Display', '6.8 inch Dynamic AMOLED 2X'),
                    ('Processor', 'Snapdragon 8 Gen 3'),
                    ('RAM', '12GB'),
                    ('Storage', '256GB'),
                    ('Camera', '200MP + 50MP + 12MP + 10MP'),
                ],
                'variants': [
                    ('256GB', 'SAM-S24U-256B', Decimal('129999')),
                    ('512GB', 'SAM-S24U-512B', Decimal('149999')),
                ],
            },
            {
                'name': 'Apple iPhone 15 Pro Max',
                'category': 'Mobile & Accessories',
                'brand': 'Apple',
                'sku': 'APL-IP15PM-256',
                'hsn': '8517',
                'desc': '6.7-inch Super Retina XDR, A17 Pro chip, 256GB. Titanium design with pro camera system.',
                'short_desc': '6.7" XDR | A17 Pro | 256GB',
                'image_key': 'iphone-15-pro',
                'price': Decimal('159900'),
                'attrs': [
                    ('Display', '6.7 inch Super Retina XDR'),
                    ('Processor', 'A17 Pro'),
                    ('Storage', '256GB'),
                    ('Camera', '48MP + 12MP + 12MP'),
                    ('Material', 'Titanium'),
                ],
                'variants': [
                    ('256GB', 'APL-IP15PM-256B', Decimal('159900')),
                    ('512GB', 'APL-IP15PM-512B', Decimal('179900')),
                ],
            },
            # Networking
            {
                'name': 'Cisco Catalyst 9300 Switch',
                'category': 'Networking Equipment',
                'brand': 'Cisco',
                'sku': 'CISCO-C9300-48',
                'hsn': '8517',
                'desc': '48-port PoE+ managed switch, ideal for enterprise networking. Stackable, secure, and reliable.',
                'short_desc': '48-Port PoE+ | Managed | Stackable',
                'image_key': 'cisco-router',
                'price': Decimal('485000'),
                'attrs': [
                    ('Ports', '48 x 1G PoE+'),
                    ('Uplink', '4 x 10G SFP+'),
                    ('PoE Budget', '437W'),
                    ('Switching Capacity', '480 Gbps'),
                ],
                'variants': [
                    ('48-Port', 'CISCO-C9300-48P', Decimal('485000')),
                    ('24-Port', 'CISCO-C9300-24P', Decimal('325000')),
                ],
            },
            {
                'name': 'TP-Link TL-SG1024DE 24-Port Switch',
                'category': 'Networking Equipment',
                'brand': 'TP-Link',
                'sku': 'TPL-SG1024DE',
                'hsn': '8517',
                'desc': '24-Port Gigabit Easy Smart Switch, plug-and-play with QoS and VLAN support.',
                'short_desc': '24-Port Gigabit | Easy Smart | QoS',
                'image_key': 'tp-link-switch',
                'price': Decimal('8499'),
                'attrs': [
                    ('Ports', '24 x 10/100/1000 Mbps'),
                    ('Switching Capacity', '48 Gbps'),
                    ('Standards', 'IEEE 802.3, 802.3u, 802.3ab'),
                ],
                'variants': [
                    ('24-Port', 'TPL-SG1024DE', Decimal('8499')),
                    ('8-Port', 'TPL-SG1008DE', Decimal('3299')),
                ],
            },
            # Audio
            {
                'name': 'Sony WH-1000XM5 Headphones',
                'category': 'Audio & Video',
                'brand': 'Sony',
                'sku': 'SONY-WH1000XM5',
                'hsn': '8518',
                'desc': 'Industry-leading noise cancellation with Auto NC Optimizer. Crystal clear hands-free calling.',
                'short_desc': 'ANC | 30hr Battery | Hi-Res Audio',
                'image_key': 'sony-headphones',
                'price': Decimal('29990'),
                'attrs': [
                    ('Type', 'Over-Ear Wireless'),
                    ('ANC', 'Yes - Industry Leading'),
                    ('Battery', '30 hours'),
                    ('Driver', '30mm'),
                    ('Weight', '250g'),
                ],
                'variants': [
                    ('Black', 'SONY-WH1000XM5-BK', Decimal('29990')),
                    ('Silver', 'SONY-WH1000XM5-SL', Decimal('29990')),
                ],
            },
            {
                'name': 'JBL Charge 5 Bluetooth Speaker',
                'category': 'Audio & Video',
                'brand': 'JBL',
                'sku': 'JBL-CHARGE5',
                'hsn': '8518',
                'desc': 'Portable Bluetooth speaker with IP67 waterproof and dustproof rating. 20 hours of playtime.',
                'short_desc': 'IP67 | 20hr Battery | Powerbank',
                'image_key': 'jbl-speaker',
                'price': Decimal('17999'),
                'attrs': [
                    ('Type', 'Portable Bluetooth'),
                    ('Waterproof', 'IP67'),
                    ('Battery', '20 hours'),
                    ('Output', '30W'),
                ],
                'variants': [
                    ('Blue', 'JBL-CHARGE5-BL', Decimal('17999')),
                    ('Red', 'JBL-CHARGE5-RD', Decimal('17999')),
                ],
            },
            # Security
            {
                'name': 'Hikvision DS-2CD2T47 4MP CCTV Camera',
                'category': 'Security Systems',
                'brand': 'Hikvision',
                'sku': 'HIK-DS2CD2T47',
                'hsn': '8525',
                'desc': '4MP Turbo HD ColorVu Fixed Bullet Camera with 40m IR. Smart detection and ANPR.',
                'short_desc': '4MP | ColorVu | 40m IR | IP67',
                'image_key': 'hikvision-cctv',
                'price': Decimal('5999'),
                'attrs': [
                    ('Resolution', '4MP (2560x1440)'),
                    ('IR Range', '40m'),
                    ('Lens', '2.8mm/4mm/6mm'),
                    ('Storage', 'Up to 256GB microSD'),
                    ('Waterproof', 'IP67'),
                ],
                'variants': [
                    ('2.8mm', 'HIK-DS2CD2T47-28', Decimal('5999')),
                    ('4mm', 'HIK-DS2CD2T47-40', Decimal('5999')),
                ],
            },
            # Storage
            {
                'name': 'Samsung 990 Pro 1TB NVMe SSD',
                'category': 'Storage & Memory',
                'brand': 'Samsung',
                'sku': 'SAM-990PRO-1TB',
                'hsn': '8523',
                'desc': 'PCIe 4.0 NVMe M.2 SSD with sequential read/write speeds up to 7,450/6,900 MB/s.',
                'short_desc': '1TB | PCIe 4.0 | 7450 MB/s Read',
                'image_key': 'samsung-ssd',
                'price': Decimal('10999'),
                'attrs': [
                    ('Capacity', '1TB'),
                    ('Interface', 'PCIe 4.0 x4 NVMe'),
                    ('Sequential Read', '7,450 MB/s'),
                    ('Sequential Write', '6,900 MB/s'),
                    ('TBW', '600 TBW'),
                ],
                'variants': [
                    ('1TB', 'SAM-990PRO-1T', Decimal('10999')),
                    ('2TB', 'SAM-990PRO-2T', Decimal('19999')),
                ],
            },
            # Printers
            {
                'name': 'HP LaserJet Pro M404dn Printer',
                'category': 'Printers & Scanners',
                'brand': 'HP',
                'sku': 'HP-LJM404DN',
                'hsn': '8443',
                'desc': 'Mono laser printer with duplex printing. Print speed up to 38 ppm.',
                'short_desc': 'Mono Laser | Duplex | 38 ppm',
                'image_key': 'hp-printer',
                'price': Decimal('32999'),
                'attrs': [
                    ('Type', 'Mono Laser'),
                    ('Print Speed', '38 ppm'),
                    ('Resolution', '4800 x 600 dpi'),
                    ('Paper Size', 'A4'),
                    ('Duplex', 'Yes'),
                ],
                'variants': [
                    ('Standard', 'HP-LJM404DN-S', Decimal('32999')),
                ],
            },
            # Power
            {
                'name': 'APC Smart-UPS 1500VA Rack Mount',
                'category': 'Power & UPS',
                'brand': 'APC',
                'sku': 'APC-SMT1500',
                'hsn': '8504',
                'desc': '1500VA / 1000W Line-interactive UPS with SmartConnect. LCD display and network management.',
                'short_desc': '1500VA | 1000W | Line-Interactive',
                'image_key': 'apc-ups',
                'price': Decimal('54999'),
                'attrs': [
                    ('Capacity', '1500VA / 1000W'),
                    ('Type', 'Line-Interactive'),
                    ('Outlets', '8 x NEMA 5-15R'),
                    ('Battery Runtime', '10 min at full load'),
                    ('Management', 'SmartConnect'),
                ],
                'variants': [
                    ('1500VA', 'APC-SMT1500-15', Decimal('54999')),
                    ('1000VA', 'APC-SMT1000-10', Decimal('39999')),
                ],
            },
            # Accessories
            {
                'name': 'Logitech MX Master 3S Mouse',
                'category': 'Computer Accessories',
                'brand': 'Logitech',
                'sku': 'LOG-MXM3S',
                'hsn': '8471',
                'desc': 'Wireless performance mouse with MagSpeed scroll wheel and 8K DPI sensor.',
                'short_desc': 'Wireless | 8K DPI | USB-C | Multi-Device',
                'image_key': 'logitech-mouse',
                'price': Decimal('9995'),
                'attrs': [
                    ('Sensor', '8K DPI'),
                    ('Connectivity', 'Bluetooth / USB-C'),
                    ('Battery', '70 days'),
                    ('Scroll', 'MagSpeed Electromagnetic'),
                    ('Weight', '141g'),
                ],
                'variants': [
                    ('Graphite', 'LOG-MXM3S-GY', Decimal('9995')),
                    ('Pale Gray', 'LOG-MXM3S-PG', Decimal('9995')),
                ],
            },
        ]

        self.products = []
        for pd in products_data:
            product = Product.objects.create(
                name=pd['name'],
                description=pd['desc'],
                short_description=pd['short_desc'],
                category=self.categories[pd['category']],
                brand=self.brands.get(pd['brand']),
                sku=pd['sku'],
                hsn_code=pd['hsn'],
                taxable=True,
                is_active=True,
                is_featured=random.choice([True, False]),
                min_selling_price=pd['price'],
                max_selling_price=pd['price'] * Decimal('1.2'),
                total_sellers=random.randint(2, 5),
                total_stock=random.randint(50, 500),
            )

            # Add images
            images = PRODUCT_IMAGES.get(pd['image_key'], PRODUCT_IMAGES['dell-latitude-5540'])
            for idx, img_url in enumerate(images):
                ProductImage.objects.create(
                    product=product,
                    image_url=img_url,
                    alt_text=f'{pd["name"]} image {idx+1}',
                    is_primary=(idx == 0),
                    sort_order=idx,
                )

            # Add attributes
            for idx, (key, value) in enumerate(pd['attrs']):
                ProductAttribute.objects.create(
                    product=product,
                    key=key,
                    value=value,
                    sort_order=idx,
                )

            # Add variants
            product_variants = []
            for v_name, v_sku, v_price in pd['variants']:
                variant = ProductVariant.objects.create(
                    product=product,
                    sku=v_sku,
                    name=v_name,
                    description=f'{pd["name"]} - {v_name}',
                    min_selling_price=v_price,
                    max_selling_price=v_price * Decimal('1.15'),
                    total_sellers=random.randint(2, 5),
                    total_stock=random.randint(30, 200),
                )
                VariantAttribute.objects.create(
                    variant=variant,
                    attribute_name='Configuration',
                    attribute_value=v_name,
                )
                for idx, img_url in enumerate(images[:1]):
                    VariantImage.objects.create(
                        variant=variant,
                        image_url=img_url,
                        alt_text=f'{pd["name"]} {v_name}',
                        is_primary=True,
                        sort_order=idx,
                    )
                product_variants.append((variant, v_price))

            self.products.append({
                'product': product,
                'variants': product_variants,
            })
            self.stdout.write(f'  [OK] {pd["name"]}')

    def _create_seller_data(self):
        self.stdout.write('\n5. Creating seller pricing...')

        for seller_data in self.sellers:
            seller = seller_data['profile']
            warehouse = seller_data['warehouse']

            # Each seller gets random products
            seller_products = random.sample(self.products, min(8, len(self.products)))

            for prod_data in seller_products:
                for variant, base_price in prod_data['variants']:
                    # Vary price slightly per seller
                    price_variation = Decimal(str(round(random.uniform(0.95, 1.08), 2)))
                    selling_price = (base_price * price_variation).quantize(Decimal('0.01'))
                    offer_price = (selling_price * Decimal('0.95')).quantize(Decimal('0.01')) if random.random() > 0.5 else None

                    pricing = SellerPricing.objects.create(
                        seller=seller,
                        variant=variant,
                        warehouse=warehouse,
                        selling_price=selling_price,
                        offer_price=offer_price,
                        tax_rate=Decimal('18.00'),
                        tax_inclusive=False,
                        shipping_charge=Decimal('0.00'),
                        free_shipping=(selling_price > Decimal('5000')),
                        minimum_order_quantity=1,
                        max_order_quantity=random.randint(100, 1000),
                        warranty_type='Manufacturer',
                        warranty_period='1 Year',
                        delivery_time_days=random.randint(2, 7),
                        estimated_delivery=f'{random.randint(2,7)} business days',
                        is_active=True,
                    )

                    # Create wholesale tiers
                    base = float(selling_price)
                    tiers = [
                        (1, 10, base),
                        (11, 50, base * 0.95),
                        (51, 200, base * 0.88),
                        (201, None, base * 0.82),
                    ]
                    for min_q, max_q, tier_price in tiers:
                        discount_pct = round((1 - tier_price / base) * 100, 2)
                        WholesaleTier.objects.create(
                            pricing=pricing,
                            min_quantity=min_q,
                            max_quantity=max_q,
                            price_per_unit=Decimal(str(round(tier_price, 2))),
                            discount_percent=Decimal(str(discount_pct)),
                            notes=f'Buy {min_q}+ units',
                        )

        self.stdout.write(f'  [OK] Created pricing for all sellers')

    def _create_inventory(self):
        self.stdout.write('\n6. Creating inventory...')

        for seller_data in self.sellers:
            seller = seller_data['profile']
            warehouse = seller_data['warehouse']

            seller_pricings = SellerPricing.objects.filter(seller=seller)
            for pricing in seller_pricings:
                stock = random.randint(20, 500)
                inv = Inventory.objects.create(
                    seller=seller,
                    variant=pricing.variant,
                    warehouse=warehouse,
                    total_stock=stock,
                    reserved_stock=random.randint(0, min(10, stock)),
                    low_stock_threshold=10,
                )
                StockHistory.objects.create(
                    inventory=inv,
                    change_type='add',
                    quantity_change=stock,
                    previous_stock=0,
                    new_stock=stock,
                    notes='Initial stock',
                )

        self.stdout.write(f'  [OK] Created inventory records')

    def _create_cart_data(self):
        self.stdout.write('\n7. Creating cart items...')

        for buyer in self.buyers[:3]:
            cart = Cart.objects.get(buyer=buyer)
            # Add 2-4 random items
            items_to_add = random.sample(self.products, min(random.randint(2, 4), len(self.products)))
            for prod_data in items_to_add:
                variant, price = random.choice(prod_data['variants'])
                seller_data = random.choice(self.sellers)
                quantity = random.randint(1, 5)
                CartItem.objects.create(
                    cart=cart,
                    seller=seller_data['profile'],
                    variant=variant,
                    quantity=quantity,
                    unit_price=price,
                    tax_rate=Decimal('18.00'),
                    total_price=price * quantity,
                )

        self.stdout.write(f'  [OK] Created cart items')

    def _create_orders(self):
        self.stdout.write('\n8. Creating orders...')

        statuses = ['pending', 'confirmed', 'processing', 'shipped', 'delivered']
        payment_statuses = ['pending', 'paid', 'paid', 'paid']

        order_num = 1
        for buyer in self.buyers:
            addresses = list(buyer.addresses.all())
            if not addresses:
                continue

            shipping = addresses[0]
            billing = addresses[0] if len(addresses) < 2 else addresses[1]

            # Create 2-3 orders per buyer
            for _ in range(random.randint(2, 3)):
                status = random.choice(statuses)
                payment_status = random.choice(payment_statuses)

                # Pick 1-3 products for this order
                order_products = random.sample(self.products, random.randint(1, 3))
                subtotal = Decimal('0')
                total_tax = Decimal('0')
                order_items_data = []

                for prod_data in order_products:
                    variant, price = random.choice(prod_data['variants'])
                    seller_data = random.choice(self.sellers)
                    qty = random.randint(1, 5)
                    item_total = price * qty
                    tax = (item_total * Decimal('0.18')).quantize(Decimal('0.01'))
                    subtotal += item_total
                    total_tax += tax
                    order_items_data.append({
                        'seller': seller_data['profile'],
                        'variant': variant,
                        'product': prod_data['product'],
                        'qty': qty,
                        'price': price,
                        'tax': tax,
                        'item_total': item_total + tax,
                    })

                total_amount = subtotal + total_tax

                order = Order.objects.create(
                    order_number=f'ORD-{timezone.now().strftime("%Y%m")}-{buyer.id.hex[:4]}-{order_num:04d}',
                    buyer=buyer,
                    status=status,
                    payment_status=payment_status,
                    billing_address=billing,
                    shipping_address=shipping,
                    subtotal=subtotal,
                    total_tax=total_tax,
                    total_shipping=Decimal('0.00'),
                    total_discount=Decimal('0.00'),
                    total_amount=total_amount,
                    notes='Please deliver during business hours' if random.random() > 0.5 else None,
                    delivered_at=timezone.now() - timedelta(days=random.randint(1, 30)) if status == 'delivered' else None,
                )

                # Create order items
                for item_data in order_items_data:
                    OrderItem.objects.create(
                        order=order,
                        seller=item_data['seller'],
                        variant=item_data['variant'],
                        product_name=item_data['product'].name,
                        variant_name=item_data['variant'].name,
                        product_image=PRODUCT_IMAGES.get('dell-latitude-5540', [''])[0],
                        quantity=item_data['qty'],
                        unit_price=item_data['price'],
                        tax_rate=Decimal('18.00'),
                        tax_amount=item_data['tax'],
                        total_price=item_data['item_total'],
                        status=status,
                    )

                # Create seller orders (one per unique seller)
                unique_sellers = set(item['seller'].id for item in order_items_data)
                for seller_id in unique_sellers:
                    seller = SellerProfile.objects.get(id=seller_id)
                    seller_items = [i for i in order_items_data if i['seller'].id == seller_id]
                    seller_subtotal = sum(i['price'] * i['qty'] for i in seller_items)
                    seller_tax = sum(i['tax'] for i in seller_items)

                    SellerOrder.objects.create(
                        order=order,
                        seller=seller,
                        status=status,
                        subtotal=seller_subtotal,
                        total_tax=seller_tax,
                        total_shipping=Decimal('0.00'),
                        total_amount=seller_subtotal + seller_tax,
                        warehouse=self.sellers[0]['warehouse'],
                    )

                    # Create invoice
                    inv_num = f'INV-{timezone.now().strftime("%Y%m")}-{order_num:04d}-{seller.id.hex[:4]}'
                    Invoice.objects.create(
                        invoice_number=inv_num,
                        order=order,
                        seller=seller,
                        buyer=buyer,
                        subtotal=seller_subtotal,
                        total_tax=seller_tax,
                        total_amount=seller_subtotal + seller_tax,
                        status='paid' if payment_status == 'paid' else 'generated',
                        issued_at=timezone.now(),
                    )

                order_num += 1

        self.stdout.write(f'  [OK] Created {order_num - 1} orders')

    def _create_reviews(self):
        self.stdout.write('\n9. Creating reviews...')

        review_titles = [
            'Excellent product!', 'Good value for money', 'Highly recommended',
            'Best in class', 'Very satisfied', 'Works perfectly',
            'Great quality', 'Fast delivery', 'Worth the price',
            'Amazing performance', 'Top notch', 'Impressive build quality',
        ]

        review_comments = [
            'This product exceeded my expectations. Build quality is excellent and performance is outstanding.',
            'Great value for money. Ordered in bulk and saved a lot. Will order again.',
            'Fast delivery and good packaging. Product works as described. Happy with the purchase.',
            'Been using this for 3 months now, no issues at all. Highly recommended for businesses.',
            'Excellent quality and competitive pricing. The wholesale discount made it even better.',
            'Perfect for our office setup. Bulk ordering was smooth and delivery was on time.',
            'Very good product for the price. Minor packaging issue but product was fine.',
            'Regular customer, never disappointed. Consistent quality and reliable delivery.',
        ]

        for buyer in self.buyers[:4]:
            orders = Order.objects.filter(buyer=buyer, status='delivered')
            for order in orders[:2]:
                for item in order.items.all():
                    if random.random() > 0.3:  # 70% chance of review
                        ProductReview.objects.create(
                            product=Product.objects.filter(sku__startswith=item.product_name[:4].upper()).first() or Product.objects.first(),
                            variant=item.variant,
                            buyer=buyer,
                            order_item=item,
                            seller=item.seller,
                            rating=random.randint(3, 5),
                            title=random.choice(review_titles),
                            comment=random.choice(review_comments),
                            is_verified=True,
                        )

            # Seller reviews
            if orders.exists():
                order = orders.first()
                seller_order = order.seller_orders.first()
                if seller_order:
                    SellerReview.objects.create(
                        seller=seller_order.seller,
                        buyer=buyer,
                        order=order,
                        rating=random.randint(4, 5),
                        title='Great seller!',
                        comment='Professional service, fast shipping, and good communication.',
                        is_verified=True,
                    )

        self.stdout.write(f'  [OK] Created reviews')

    def _create_notifications(self):
        self.stdout.write('\n10. Creating notifications...')

        notification_templates = [
            ('order', 'Order Confirmed', 'Your order {order_number} has been confirmed and is being processed.'),
            ('order', 'Order Shipped', 'Great news! Your order {order_number} has been shipped. Track your package.'),
            ('order', 'Order Delivered', 'Your order {order_number} has been delivered successfully.'),
            ('promotion', 'Summer Sale!', 'Get up to 30% off on all networking equipment. Limited time offer!'),
            ('promotion', 'Bulk Discount Available', 'Order 50+ units and get exclusive wholesale pricing.'),
            ('system', 'Welcome to B2B Market!', 'Thank you for joining. Explore thousands of products at wholesale prices.'),
            ('system', 'Profile Verification', 'Your business profile has been verified. Enjoy trusted seller benefits.'),
            ('seller', 'New Order Received', 'You have a new order {order_number}. Please confirm within 24 hours.'),
            ('seller', 'Low Stock Alert', 'Some products are running low on stock. Reorder soon.'),
        ]

        all_users = list(User.objects.filter(is_active=True))
        for user in all_users[:10]:
            num_notifications = random.randint(3, 6)
            for _ in range(num_notifications):
                ntype, title, message = random.choice(notification_templates)
                Notification.objects.create(
                    user=user,
                    notification_type=ntype,
                    title=title,
                    message=message.replace('{order_number}', f'ORD-{random.randint(1000,9999)}'),
                    is_read=random.choice([True, True, False]),
                )

        self.stdout.write(f'  [OK] Created notifications')

    def _print_summary(self):
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS('SEED DATA SUMMARY'))
        self.stdout.write('=' * 60)
        self.stdout.write(f'  Users:          {User.objects.count()}')
        self.stdout.write(f'  Buyer Profiles:  {BuyerProfile.objects.count()}')
        self.stdout.write(f'  Seller Profiles: {SellerProfile.objects.count()}')
        self.stdout.write(f'  Categories:      {Category.objects.count()}')
        self.stdout.write(f'  Brands:          {Brand.objects.count()}')
        self.stdout.write(f'  Products:        {Product.objects.count()}')
        self.stdout.write(f'  Variants:        {ProductVariant.objects.count()}')
        self.stdout.write(f'  Pricing:         {SellerPricing.objects.count()}')
        self.stdout.write(f'  Wholesale Tiers: {WholesaleTier.objects.count()}')
        self.stdout.write(f'  Inventory:       {Inventory.objects.count()}')
        self.stdout.write(f'  Cart Items:      {CartItem.objects.count()}')
        self.stdout.write(f'  Orders:          {Order.objects.count()}')
        self.stdout.write(f'  Order Items:     {OrderItem.objects.count()}')
        self.stdout.write(f'  Reviews:         {ProductReview.objects.count()}')
        self.stdout.write(f'  Notifications:   {Notification.objects.count()}')
        self.stdout.write('=' * 60)

        self.stdout.write(self.style.SUCCESS('\nLOGIN CREDENTIALS:'))
        self.stdout.write('  Admin:   himanshu@admin.com / himanshu')
        self.stdout.write('  Buyers:  ravi@buyer.com, priya@buyer.com, amit@buyer.com, etc. / buyer123')
        self.stdout.write('  Sellers: techhub@seller.com, digital@seller.com, circuit@seller.com / seller123')
        self.stdout.write('=' * 60)
