"""
Product catalog data for B2B Electronics Marketplace.
500+ products across 18 categories with realistic brands, specs, and pricing.
"""

# Unsplash image URLs by product type (reliable, royalty-free)
IMAGES = {
    'laptop': [
        'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=600&q=80',
        'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=600&q=80',
        'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&q=80',
    ],
    'desktop': [
        'https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=600&q=80',
        'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=600&q=80',
    ],
    'keyboard': [
        'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=600&q=80',
        'https://images.unsplash.com/photo-1618384887929-16ec33fab9ef?w=600&q=80',
    ],
    'mouse': [
        'https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=600&q=80',
    ],
    'monitor': [
        'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=600&q=80',
        'https://images.unsplash.com/photo-1585792180666-f7347c490ee2?w=600&q=80',
    ],
    'processor': [
        'https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=600&q=80',
    ],
    'gpu': [
        'https://images.unsplash.com/photo-1591488320449-011701bb6704?w=600&q=80',
        'https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=600&q=80',
    ],
    'motherboard': [
        'https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&q=80',
    ],
    'ram': [
        'https://images.unsplash.com/photo-1562976540-1502c2145186?w=600&q=80',
    ],
    'ssd': [
        'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?w=600&q=80',
    ],
    'hdd': [
        'https://images.unsplash.com/photo-1597858520171-563a8e8b9925?w=600&q=80',
    ],
    'router': [
        'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&q=80',
        'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=600&q=80',
    ],
    'switch': [
        'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&q=80',
    ],
    'camera': [
        'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=600&q=80',
        'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=600&q=80',
    ],
    'cctv': [
        'https://images.unsplash.com/photo-1557597774-9d273605dfa9?w=600&q=80',
    ],
    'printer': [
        'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=600&q=80',
    ],
    'headphones': [
        'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&q=80',
        'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=600&q=80',
    ],
    'speaker': [
        'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=600&q=80',
        'https://images.unsplash.com/photo-1545454675-3531b543be5d?w=600&q=80',
    ],
    'earbuds': [
        'https://images.unsplash.com/photo-1590658268037-6bf12f032f55?w=600&q=80',
    ],
    'microphone': [
        'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=600&q=80',
    ],
    'projector': [
        'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=600&q=80',
    ],
    'ups': [
        'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&q=80',
    ],
    'inverter': [
        'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&q=80',
    ],
    'smartphone': [
        'https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=600&q=80',
        'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600&q=80',
    ],
    'tablet': [
        'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=600&q=80',
    ],
    'smartwatch': [
        'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&q=80',
    ],
    'powerbank': [
        'https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=600&q=80',
    ],
    'charger': [
        'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=600&q=80',
    ],
    'cable': [
        'https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=600&q=80',
    ],
    'server': [
        'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&q=80',
    ],
    'industrial': [
        'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80',
    ],
    'webcam': [
        'https://images.unsplash.com/photo-1587826080692-f439cd0b70da?w=600&q=80',
    ],
    'cabinet': [
        'https://images.unsplash.com/photo-1587202372775-e229f172b9d7?w=600&q=80',
    ],
    'default': [
        'https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&q=80',
    ],
}

BRANDS = [
    ('Dell', 'USA', 1984, True, 'American multinational computer technology company'),
    ('HP', 'USA', 1939, True, 'Hewlett-Packard - Leading technology company'),
    ('Lenovo', 'China', 1984, True, 'Chinese multinational technology company'),
    ('Apple', 'USA', 1976, True, 'American multinational technology company'),
    ('Samsung', 'South Korea', 1938, True, 'South Korean multinational electronics company'),
    ('Cisco', 'USA', 1984, True, 'American multinational technology conglomerate'),
    ('TP-Link', 'China', 1996, True, 'Chinese networking equipment manufacturer'),
    ('Sony', 'Japan', 1946, True, 'Japanese multinational conglomerate'),
    ('JBL', 'USA', 1946, False, 'American audio electronics company'),
    ('Hikvision', 'China', 2001, True, 'Video surveillance equipment manufacturer'),
    ('Logitech', 'Switzerland', 1981, True, 'Swiss computer peripherals manufacturer'),
    ('APC', 'USA', 1981, True, 'American manufacturer of UPS systems'),
    ('Intel', 'USA', 1968, True, 'American multinational semiconductor company'),
    ('AMD', 'USA', 1969, True, 'American multinational semiconductor company'),
    ('NVIDIA', 'USA', 1993, True, 'American GPU leader'),
    ('Corsair', 'USA', 1994, True, 'Computer peripherals and gaming gear'),
    ('Seagate', 'USA', 1978, True, 'American data storage company'),
    ('Western Digital', 'USA', 1970, True, 'American data storage company'),
    ('Kingston', 'USA', 1987, True, 'American memory and storage products'),
    ('ASUS', 'Taiwan', 1989, True, 'Taiwanese multinational computer company'),
    ('MSI', 'Taiwan', 1986, True, 'Taiwanese IT corporation'),
    ('Epson', 'Japan', 1942, True, 'Japanese electronics company'),
    ('Brother', 'Japan', 1908, False, 'Japanese electronics company'),
    ('Zebronics', 'India', 1997, False, 'Indian IT peripherals company'),
    ('D-Link', 'Taiwan', 1986, False, 'Taiwanese networking equipment'),
    ('CP Plus', 'India', 2007, False, 'Indian security solutions'),
    ('Honeywell', 'USA', 1906, True, 'American multinational conglomerate'),
    ('Bosch', 'Germany', 1886, True, 'German engineering company'),
    ('Siemens', 'Germany', 1847, True, 'German technology company'),
    ('Schneider Electric', 'France', 1836, False, 'French electrical equipment company'),
    ('ABB', 'Switzerland', 1988, False, 'Swedish-Swiss electrical engineering'),
    ('Panasonic', 'Japan', 1918, True, 'Japanese electronics corporation'),
    ('Bose', 'USA', 1964, True, 'American audio equipment company'),
    ('Razer', 'USA', 2005, True, 'Gaming hardware and peripherals'),
]

# Product data: (name, brand, sku, short_desc, retail_price, moq, gst, warranty, country, img_key, specs)
# Category is determined by which dict key this appears under
PRODUCTS = {
    'Business Laptops': [
        ('Dell Latitude 5540 Business Laptop', 'Dell', 'DELL-LAT5540', '15.6" FHD | i7-1365U | 16GB | 512GB SSD', 89999, 1, 18, '3 Years', 'China', 'laptop', {'Display': '15.6" FHD 1920x1080', 'Processor': 'Intel Core i7-1365U', 'RAM': '16GB DDR4 3200MHz', 'Storage': '512GB NVMe PCIe Gen4', 'OS': 'Windows 11 Pro', 'Weight': '1.76 kg'}),
        ('Dell Latitude 5540 i5', 'Dell', 'DELL-LAT5540I5', '15.6" FHD | i5-1335U | 8GB | 256GB SSD', 62999, 1, 18, '3 Years', 'China', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Core i5-1335U', 'RAM': '8GB DDR4', 'Storage': '256GB NVMe SSD'}),
        ('Dell Vostro 3420 Laptop', 'Dell', 'DELL-VOS3420', '14" FHD | i3-1215U | 8GB | 512GB SSD', 42999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '14" FHD', 'Processor': 'Intel Core i3-1215U', 'RAM': '8GB DDR4', 'Storage': '512GB SSD'}),
        ('Dell Inspiron 15 3520', 'Dell', 'DELL-INS3520', '15.6" FHD | i5-1235U | 8GB | 512GB SSD', 48999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Core i5-1235U', 'RAM': '8GB DDR4', 'Storage': '512GB SSD'}),
        ('HP ProBook 450 G10', 'HP', 'HP-PB450G10', '15.6" FHD | i5-1335U | 8GB | 512GB SSD', 58999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Core i5-1335U', 'RAM': '8GB DDR4', 'Storage': '512GB NVMe SSD'}),
        ('HP ProBook 450 G10 i7', 'HP', 'HP-PB450G10I7', '15.6" FHD | i7-1355U | 16GB | 512GB SSD', 78999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Core i7-1355U', 'RAM': '16GB DDR4', 'Storage': '512GB NVMe SSD'}),
        ('HP EliteBook 840 G10', 'HP', 'HP-EB840G10', '14" WQXGA | i7-1365U | 16GB | 512GB SSD', 119999, 1, 18, '3 Years', 'China', 'laptop', {'Display': '14" WQXGA 2560x1600', 'Processor': 'Intel Core i7-1365U', 'RAM': '16GB DDR5', 'Weight': '1.36 kg'}),
        ('HP 245 G9 Laptop', 'HP', 'HP-245G9', '14" HD | Athlon Silver | 4GB | 256GB SSD', 27999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '14" HD', 'Processor': 'AMD Athlon Silver 3050U', 'RAM': '4GB DDR4', 'Storage': '256GB SSD'}),
        ('Lenovo ThinkPad X1 Carbon G11', 'Lenovo', 'LEN-X1CG11', '14" 2.8K OLED | i7-1365U | 16GB | 512GB', 139999, 1, 18, '3 Years', 'China', 'laptop', {'Display': '14" 2.8K OLED', 'Processor': 'Intel Core i7-1365U', 'RAM': '16GB LPDDR5', 'Weight': '1.12 kg'}),
        ('Lenovo ThinkPad E16 G2', 'Lenovo', 'LEN-E16G2', '16" WUXGA | i5-1335U | 8GB | 512GB SSD', 56999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '16" WUXGA', 'Processor': 'Intel Core i5-1335U', 'RAM': '8GB DDR4', 'Storage': '512GB SSD'}),
        ('Lenovo IdeaPad Slim 3', 'Lenovo', 'LEN-SLIM3', '15.6" FHD | i5-1235U | 8GB | 512GB SSD', 44999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Core i5-1235U', 'RAM': '8GB DDR4', 'Storage': '512GB SSD'}),
        ('Lenovo V15 G4', 'Lenovo', 'LEN-V15G4', '15.6" FHD | i3-1315U | 8GB | 256GB SSD', 34999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Core i3-1315U', 'RAM': '8GB DDR4', 'Storage': '256GB SSD'}),
        ('ASUS ExpertBook B1', 'ASUS', 'ASUS-EB1', '15.6" FHD | i5-1335U | 8GB | 512GB SSD', 52999, 1, 18, '1 Year', 'Taiwan', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Core i5-1335U', 'RAM': '8GB DDR4', 'Storage': '512GB SSD'}),
        ('ASUS Vivobook 15', 'ASUS', 'ASUS-VB15', '15.6" FHD | i7-1355U | 16GB | 512GB SSD', 64999, 1, 18, '1 Year', 'Taiwan', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Core i7-1355U', 'RAM': '16GB DDR4', 'Storage': '512GB SSD'}),
    ],
    'Gaming Laptops': [
        ('Dell G15 5530 Gaming', 'Dell', 'DELL-G155530', '15.6" FHD 120Hz | i7-13650HX | 16GB | 512GB | RTX 4060', 104999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD 120Hz', 'Processor': 'Intel Core i7-13650HX', 'RAM': '16GB DDR5', 'GPU': 'NVIDIA RTX 4060 8GB', 'Storage': '512GB NVMe SSD'}),
        ('Dell Alienware m16', 'Dell', 'DELL-AW-M16', '16" QHD 165Hz | i9-13900HX | 32GB | 1TB | RTX 4080', 249999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '16" QHD 165Hz', 'Processor': 'Intel Core i9-13900HX', 'RAM': '32GB DDR5', 'GPU': 'NVIDIA RTX 4080 12GB', 'Storage': '1TB NVMe SSD'}),
        ('HP Victus 15 Gaming', 'HP', 'HP-VICT15', '15.6" FHD 144Hz | i5-13500H | 8GB | 512GB | RTX 3050', 64999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD 144Hz', 'Processor': 'Intel Core i5-13500H', 'RAM': '8GB DDR5', 'GPU': 'NVIDIA RTX 3050 6GB', 'Storage': '512GB NVMe SSD'}),
        ('HP Omen 16 Gaming', 'HP', 'HP-OMEN16', '16.1" QHD 165Hz | i7-13700HX | 16GB | 1TB | RTX 4070', 144999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '16.1" QHD 165Hz', 'Processor': 'Intel Core i7-13700HX', 'RAM': '16GB DDR5', 'GPU': 'NVIDIA RTX 4070 8GB', 'Storage': '1TB NVMe SSD'}),
        ('Lenovo Legion 5 Pro', 'Lenovo', 'LEN-LEG5P', '16" WQXGA 165Hz | i7-13700H | 16GB | 1TB | RTX 4060', 129999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '16" WQXGA 165Hz', 'Processor': 'Intel Core i7-13700H', 'RAM': '16GB DDR5', 'GPU': 'NVIDIA RTX 4060 8GB', 'Storage': '1TB NVMe SSD'}),
        ('Lenovo IdeaPad Gaming 3', 'Lenovo', 'LEN-IPG3', '15.6" FHD 120Hz | i5-12500H | 8GB | 512GB | RTX 3050', 57999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD 120Hz', 'Processor': 'Intel Core i5-12500H', 'RAM': '8GB DDR4', 'GPU': 'NVIDIA RTX 3050 4GB', 'Storage': '512GB NVMe SSD'}),
        ('ASUS TUF Gaming F15', 'ASUS', 'ASUS-TUF15', '15.6" FHD 144Hz | i7-12700H | 16GB | 512GB | RTX 4060', 94999, 1, 18, '1 Year', 'Taiwan', 'laptop', {'Display': '15.6" FHD 144Hz', 'Processor': 'Intel Core i7-12700H', 'RAM': '16GB DDR5', 'GPU': 'NVIDIA RTX 4060 8GB', 'Storage': '512GB NVMe SSD'}),
        ('ASUS ROG Strix G16', 'ASUS', 'ASUS-ROG-G16', '16" FHD 165Hz | i9-13980HX | 32GB | 1TB | RTX 4070', 174999, 1, 18, '1 Year', 'Taiwan', 'laptop', {'Display': '16" FHD 165Hz', 'Processor': 'Intel Core i9-13980HX', 'RAM': '32GB DDR5', 'GPU': 'NVIDIA RTX 4070 8GB', 'Storage': '1TB NVMe SSD'}),
        ('MSI Katana 15 Gaming', 'MSI', 'MSI-KAT15', '15.6" FHD 144Hz | i7-13620H | 16GB | 512GB | RTX 4060', 89999, 1, 18, '1 Year', 'Taiwan', 'laptop', {'Display': '15.6" FHD 144Hz', 'Processor': 'Intel Core i7-13620H', 'RAM': '16GB DDR5', 'GPU': 'NVIDIA RTX 4060 8GB', 'Storage': '512GB NVMe SSD'}),
        ('MSI Raider GE78 HX', 'MSI', 'MSI-RAIDER78', '17.3" QHD 240Hz | i9-13950HX | 64GB | 2TB | RTX 4090', 349999, 1, 18, '1 Year', 'Taiwan', 'laptop', {'Display': '17.3" QHD 240Hz', 'Processor': 'Intel Core i9-13950HX', 'RAM': '64GB DDR5', 'GPU': 'NVIDIA RTX 4090 16GB', 'Storage': '2TB NVMe SSD'}),
        ('Razer Blade 15 Gaming', 'Razer', 'RZR-BLADE15', '15.6" QHD 240Hz | i7-13800H | 16GB | 1TB | RTX 4070', 199999, 1, 18, '1 Year', 'USA', 'laptop', {'Display': '15.6" QHD 240Hz', 'Processor': 'Intel Core i7-13800H', 'RAM': '16GB DDR5', 'GPU': 'NVIDIA RTX 4070 8GB', 'Storage': '1TB NVMe SSD', 'Weight': '2.01 kg'}),
    ],
    'Desktop PCs': [
        ('Dell OptiPlex 7010 SFF', 'Dell', 'DELL-OPT7010', 'i5-13500 | 8GB | 256GB SSD | Win 11 Pro', 52999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i5-13500', 'RAM': '8GB DDR5', 'Storage': '256GB NVMe SSD', 'Form Factor': 'Small Form Factor'}),
        ('Dell OptiPlex 7010 Tower', 'Dell', 'DELL-OPT7010T', 'i7-13700 | 16GB | 512GB SSD | Win 11 Pro', 74999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i7-13700', 'RAM': '16GB DDR5', 'Storage': '512GB NVMe SSD', 'Form Factor': 'Tower'}),
        ('HP Pro 400 G9 SFF', 'HP', 'HP-PRO400G9', 'i5-12500 | 8GB | 256GB SSD | Win 11 Pro', 48999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i5-12500', 'RAM': '8GB DDR4', 'Storage': '256GB SSD'}),
        ('HP EliteDesk 800 G9', 'HP', 'HP-ED800G9', 'i7-12700 | 16GB | 512GB SSD | Win 11 Pro', 84999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i7-12700', 'RAM': '16GB DDR5', 'Storage': '512GB NVMe SSD'}),
        ('Lenovo ThinkCentre M70q Gen 4', 'Lenovo', 'LEN-M70Q', 'i5-13400T | 8GB | 256GB SSD', 42999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i5-13400T', 'RAM': '8GB DDR5', 'Storage': '256GB NVMe SSD', 'Form Factor': 'Tiny'}),
        ('Lenovo ThinkCentre M70s Gen 4', 'Lenovo', 'LEN-M70S', 'i7-13700 | 16GB | 512GB SSD', 69999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i7-13700', 'RAM': '16GB DDR5', 'Storage': '512GB NVMe SSD'}),
        ('ASUS ExpertCenter D5 SFF', 'ASUS', 'ASUS-DCD5', 'i5-13400 | 8GB | 256GB SSD', 44999, 1, 18, '1 Year', 'Taiwan', 'desktop', {'Processor': 'Intel Core i5-13400', 'RAM': '8GB DDR4', 'Storage': '256GB SSD'}),
    ],
    'Mini PCs': [
        ('Intel NUC 13 Pro', 'Intel', 'INT-NUC13', 'i5-1340P | 8GB | 256GB SSD', 38999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i5-1340P', 'RAM': '8GB DDR4', 'Storage': '256GB NVMe SSD', 'Size': '117 x 112 x 37mm'}),
        ('Intel NUC 13 Pro i7', 'Intel', 'INT-NUC13I7', 'i7-1360P | 16GB | 512GB SSD', 56999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i7-1360P', 'RAM': '16GB DDR5', 'Storage': '512GB NVMe SSD'}),
        ('ASUS PN64 Mini PC', 'ASUS', 'ASUS-PN64', 'i7-13700H | 16GB | 512GB SSD', 62999, 1, 18, '1 Year', 'Taiwan', 'desktop', {'Processor': 'Intel Core i7-13700H', 'RAM': '16GB DDR5', 'Storage': '512GB NVMe SSD'}),
    ],
    'Graphics Cards': [
        ('NVIDIA GeForce RTX 4090', 'NVIDIA', 'NV-RTX4090', '24GB GDDR6X | DLSS 3 | Ray Tracing', 164999, 1, 18, '3 Years', 'China', 'gpu', {'GPU': 'NVIDIA GeForce RTX 4090', 'Memory': '24GB GDDR6X', 'Boost Clock': '2520 MHz', 'TDP': '450W', 'Interface': 'PCIe 4.0 x16'}),
        ('NVIDIA GeForce RTX 4080 SUPER', 'NVIDIA', 'NV-RTX4080S', '16GB GDDR6X | DLSS 3 | Ray Tracing', 99999, 1, 18, '3 Years', 'China', 'gpu', {'GPU': 'NVIDIA GeForce RTX 4080 SUPER', 'Memory': '16GB GDDR6X', 'Boost Clock': '2550 MHz', 'TDP': '320W'}),
        ('NVIDIA GeForce RTX 4070 Ti SUPER', 'NVIDIA', 'NV-RTX4070TIS', '16GB GDDR6X | DLSS 3', 79999, 1, 18, '3 Years', 'China', 'gpu', {'GPU': 'NVIDIA GeForce RTX 4070 Ti SUPER', 'Memory': '16GB GDDR6X', 'Boost Clock': '2610 MHz', 'TDP': '285W'}),
        ('NVIDIA GeForce RTX 4070', 'NVIDIA', 'NV-RTX4070', '12GB GDDR6X | DLSS 3', 54999, 1, 18, '3 Years', 'China', 'gpu', {'GPU': 'NVIDIA GeForce RTX 4070', 'Memory': '12GB GDDR6X', 'Boost Clock': '2475 MHz', 'TDP': '200W'}),
        ('NVIDIA GeForce RTX 4060 Ti', 'NVIDIA', 'NV-RTX4060TI', '8GB GDDR6 | DLSS 3', 38999, 1, 18, '3 Years', 'China', 'gpu', {'GPU': 'NVIDIA GeForce RTX 4060 Ti', 'Memory': '8GB GDDR6', 'Boost Clock': '2535 MHz', 'TDP': '160W'}),
        ('NVIDIA GeForce RTX 4060', 'NVIDIA', 'NV-RTX4060', '8GB GDDR6 | DLSS 3', 28999, 1, 18, '3 Years', 'China', 'gpu', {'GPU': 'NVIDIA GeForce RTX 4060', 'Memory': '8GB GDDR6', 'Boost Clock': '2460 MHz', 'TDP': '115W'}),
        ('AMD Radeon RX 7900 XTX', 'AMD', 'AMD-RX7900XTX', '24GB GDDR6 | Ray Tracing', 89999, 1, 18, '3 Years', 'China', 'gpu', {'GPU': 'AMD Radeon RX 7900 XTX', 'Memory': '24GB GDDR6', 'Boost Clock': '2500 MHz', 'TDP': '355W'}),
        ('AMD Radeon RX 7800 XT', 'AMD', 'AMD-RX7800XT', '16GB GDDR6 | Ray Tracing', 47999, 1, 18, '3 Years', 'China', 'gpu', {'GPU': 'AMD Radeon RX 7800 XT', 'Memory': '16GB GDDR6', 'Boost Clock': '2430 MHz', 'TDP': '263W'}),
        ('AMD Radeon RX 7600', 'AMD', 'AMD-RX7600', '8GB GDDR6 | Ray Tracing', 24999, 1, 18, '3 Years', 'China', 'gpu', {'GPU': 'AMD Radeon RX 7600', 'Memory': '8GB GDDR6', 'Boost Clock': '2655 MHz', 'TDP': '165W'}),
        ('ASUS ROG Strix RTX 4070 Ti OC', 'ASUS', 'ASUS-ROG4070TI', '12GB GDDR6X | OC Edition', 84999, 1, 18, '3 Years', 'Taiwan', 'gpu', {'GPU': 'NVIDIA GeForce RTX 4070 Ti', 'Memory': '12GB GDDR6X', 'Boost Clock': '2670 MHz', 'TDP': '285W'}),
        ('MSI GeForce RTX 4070 Ventus 3X', 'MSI', 'MSI-RTX4070V', '12GB GDDR6X | Triple Fan', 57999, 1, 18, '3 Years', 'Taiwan', 'gpu', {'GPU': 'NVIDIA GeForce RTX 4070', 'Memory': '12GB GDDR6X', 'Boost Clock': '2505 MHz', 'TDP': '200W'}),
        ('Corsair Hydro X GPU Block', 'Corsair', 'COR-HYDXGPU', 'GPU Water Block for RTX 4090', 14999, 1, 18, '2 Years', 'USA', 'gpu', {'Type': 'GPU Water Block', 'Compatible': 'RTX 4090', 'Material': 'Copper + Acrylic'}),
    ],
    'Processors': [
        ('Intel Core i9-14900K', 'Intel', 'INT-I9149K', '24-Core | 32-Thread | 6.0GHz | LGA 1700', 54999, 1, 18, '3 Years', 'Malaysia', 'processor', {'Cores': '24 (8P+16E)', 'Threads': '32', 'Base Clock': '3.2 GHz', 'Boost Clock': '6.0 GHz', 'TDP': '253W', 'Socket': 'LGA 1700'}),
        ('Intel Core i7-14700K', 'Intel', 'INT-I7147K', '20-Core | 28-Thread | 5.6GHz | LGA 1700', 36999, 1, 18, '3 Years', 'Malaysia', 'processor', {'Cores': '20 (8P+12E)', 'Threads': '28', 'Base Clock': '3.4 GHz', 'Boost Clock': '5.6 GHz', 'TDP': '253W'}),
        ('Intel Core i5-14600K', 'Intel', 'INT-I5146K', '14-Core | 20-Thread | 5.3GHz | LGA 1700', 27999, 1, 18, '3 Years', 'Malaysia', 'processor', {'Cores': '14 (6P+8E)', 'Threads': '20', 'Base Clock': '3.5 GHz', 'Boost Clock': '5.3 GHz', 'TDP': '181W'}),
        ('Intel Core i5-14400F', 'Intel', 'INT-I5144F', '10-Core | 16-Thread | 4.7GHz | LGA 1700', 16499, 1, 18, '3 Years', 'Malaysia', 'processor', {'Cores': '10 (6P+4E)', 'Threads': '16', 'Base Clock': '2.5 GHz', 'Boost Clock': '4.7 GHz', 'TDP': '148W'}),
        ('Intel Core i3-14100F', 'Intel', 'INT-I3141F', '4-Core | 8-Thread | 4.7GHz | LGA 1700', 9499, 1, 18, '3 Years', 'Malaysia', 'processor', {'Cores': '4', 'Threads': '8', 'Base Clock': '3.5 GHz', 'Boost Clock': '4.7 GHz', 'TDP': '110W'}),
        ('AMD Ryzen 9 7950X', 'AMD', 'AMD-R9795X', '16-Core | 32-Thread | 5.7GHz | AM5', 52999, 1, 18, '3 Years', 'China', 'processor', {'Cores': '16', 'Threads': '32', 'Base Clock': '4.5 GHz', 'Boost Clock': '5.7 GHz', 'TDP': '170W', 'Socket': 'AM5'}),
        ('AMD Ryzen 9 7900X', 'AMD', 'AMD-R9790X', '12-Core | 24-Thread | 5.6GHz | AM5', 39999, 1, 18, '3 Years', 'China', 'processor', {'Cores': '12', 'Threads': '24', 'Base Clock': '4.7 GHz', 'Boost Clock': '5.6 GHz', 'TDP': '170W'}),
        ('AMD Ryzen 7 7700X', 'AMD', 'AMD-R7770X', '8-Core | 16-Thread | 5.4GHz | AM5', 27999, 1, 18, '3 Years', 'China', 'processor', {'Cores': '8', 'Threads': '16', 'Base Clock': '4.5 GHz', 'Boost Clock': '5.4 GHz', 'TDP': '105W'}),
        ('AMD Ryzen 5 7600X', 'AMD', 'AMD-R5760X', '6-Core | 12-Thread | 5.3GHz | AM5', 18999, 1, 18, '3 Years', 'China', 'processor', {'Cores': '6', 'Threads': '12', 'Base Clock': '4.7 GHz', 'Boost Clock': '5.3 GHz', 'TDP': '105W'}),
        ('AMD Ryzen 5 5600X', 'AMD', 'AMD-R5560X', '6-Core | 12-Thread | 4.6GHz | AM4', 12999, 1, 18, '3 Years', 'China', 'processor', {'Cores': '6', 'Threads': '12', 'Base Clock': '3.7 GHz', 'Boost Clock': '4.6 GHz', 'TDP': '65W', 'Socket': 'AM4'}),
    ],
    'Motherboards': [
        ('ASUS ROG Strix Z790-E Gaming', 'ASUS', 'ASUS-ROGZ790E', 'LGA 1700 | DDR5 | Wi-Fi 6E | PCIe 5.0', 39999, 1, 18, '3 Years', 'Taiwan', 'motherboard', {'Socket': 'LGA 1700', 'Chipset': 'Intel Z790', 'RAM Slots': '4x DDR5', 'Max RAM': '128GB', 'PCIe': '5.0 x16', 'M.2 Slots': '4'}),
        ('MSI MAG Z790 Tomahawk WiFi', 'MSI', 'MSI-Z790TOM', 'LGA 1700 | DDR5 | Wi-Fi 6E', 29999, 1, 18, '3 Years', 'Taiwan', 'motherboard', {'Socket': 'LGA 1700', 'Chipset': 'Intel Z790', 'RAM Slots': '4x DDR5', 'Max RAM': '128GB', 'M.2 Slots': '4'}),
        ('Gigabyte B760M DS3H', 'ASUS', 'GB-B760MDS3H', 'LGA 1700 | DDR5 | Micro ATX', 12999, 1, 18, '3 Years', 'Taiwan', 'motherboard', {'Socket': 'LGA 1700', 'Chipset': 'Intel B760', 'RAM Slots': '2x DDR5', 'Max RAM': '64GB', 'Form Factor': 'Micro ATX'}),
        ('ASUS TUF Gaming B650-Plus WiFi', 'ASUS', 'ASUS-TUF650', 'AM5 | DDR5 | Wi-Fi 6E', 19999, 1, 18, '3 Years', 'Taiwan', 'motherboard', {'Socket': 'AM5', 'Chipset': 'AMD B650', 'RAM Slots': '4x DDR5', 'Max RAM': '128GB', 'M.2 Slots': '3'}),
        ('MSI MAG B650 Tomahawk WiFi', 'MSI', 'MSI-B650TOM', 'AM5 | DDR5 | Wi-Fi 6E', 21999, 1, 18, '3 Years', 'Taiwan', 'motherboard', {'Socket': 'AM5', 'Chipset': 'AMD B650', 'RAM Slots': '4x DDR5', 'Max RAM': '128GB'}),
        ('Gigabyte X670E Aorus Master', 'ASUS', 'GB-X670EAM', 'AM5 | DDR5 | PCIe 5.0', 34999, 1, 18, '3 Years', 'Taiwan', 'motherboard', {'Socket': 'AM5', 'Chipset': 'AMD X670E', 'RAM Slots': '4x DDR5', 'Max RAM': '128GB', 'PCIe': '5.0'}),
    ],
    'RAM': [
        ('Kingston Fury Beast 16GB DDR5', 'Kingston', 'KNG-FB16D5', '16GB DDR5-5200MHz | CL40', 4999, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '16GB', 'Type': 'DDR5', 'Speed': '5200 MHz', 'CAS Latency': 'CL40', 'Voltage': '1.25V'}),
        ('Kingston Fury Beast 32GB DDR5', 'Kingston', 'KNG-FB32D5', '32GB DDR5-5200MHz | CL40', 8999, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '32GB', 'Type': 'DDR5', 'Speed': '5200 MHz', 'CAS Latency': 'CL40'}),
        ('Corsair Vengeance 16GB DDR5', 'Corsair', 'COR-VEN16D5', '16GB DDR5-5600MHz | CL36', 5499, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '16GB', 'Type': 'DDR5', 'Speed': '5600 MHz', 'CAS Latency': 'CL36'}),
        ('Corsair Vengeance 32GB DDR5', 'Corsair', 'COR-VEN32D5', '32GB DDR5-5600MHz | CL36', 9999, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '32GB', 'Type': 'DDR5', 'Speed': '5600 MHz', 'CAS Latency': 'CL36'}),
        ('Corsair Dominator Platinum 32GB DDR5', 'Corsair', 'COR-DOM32D5', '32GB DDR5-6200MHz | CL36 | RGB', 16999, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '32GB', 'Type': 'DDR5', 'Speed': '6200 MHz', 'CAS Latency': 'CL36', 'RGB': 'Yes'}),
        ('Kingston Fury Beast 16GB DDR4', 'Kingston', 'KNG-FB16D4', '16GB DDR4-3200MHz | CL16', 3299, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '16GB', 'Type': 'DDR4', 'Speed': '3200 MHz', 'CAS Latency': 'CL16'}),
        ('Kingston Fury Beast 32GB DDR4', 'Kingston', 'KNG-FB32D4', '32GB DDR4-3200MHz | CL16', 5999, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '32GB', 'Type': 'DDR4', 'Speed': '3200 MHz', 'CAS Latency': 'CL16'}),
        ('Corsair Vengeance LPX 16GB DDR4', 'Corsair', 'COR-VLPX16D4', '16GB DDR4-3200MHz | CL16', 3499, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '16GB', 'Type': 'DDR4', 'Speed': '3200 MHz', 'CAS Latency': 'CL16', 'Height': '33.5mm'}),
    ],
    'SSD Drives': [
        ('Samsung 990 Pro 1TB NVMe', 'Samsung', 'SAM-990P1T', '1TB PCIe Gen4 | 7450 MB/s Read', 9999, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '1TB', 'Interface': 'PCIe Gen4 x4 NVMe', 'Sequential Read': '7450 MB/s', 'Sequential Write': '6900 MB/s', 'TBW': '600 TBW'}),
        ('Samsung 990 Pro 2TB NVMe', 'Samsung', 'SAM-990P2T', '2TB PCIe Gen4 | 7450 MB/s Read', 17999, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '2TB', 'Interface': 'PCIe Gen4 x4 NVMe', 'Sequential Read': '7450 MB/s', 'Sequential Write': '6900 MB/s'}),
        ('Samsung 980 Pro 1TB NVMe', 'Samsung', 'SAM-980P1T', '1TB PCIe Gen4 | 7000 MB/s Read', 7999, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '1TB', 'Interface': 'PCIe Gen4 x4 NVMe', 'Sequential Read': '7000 MB/s', 'Sequential Write': '5000 MB/s'}),
        ('Samsung 870 EVO 1TB SATA', 'Samsung', 'SAM-870E1T', '1TB SATA III | 560 MB/s Read', 6499, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '1TB', 'Interface': 'SATA III 6Gb/s', 'Sequential Read': '560 MB/s', 'Sequential Write': '530 MB/s'}),
        ('WD Black SN850X 1TB NVMe', 'Western Digital', 'WD-SN850X1T', '1TB PCIe Gen4 | 7300 MB/s Read', 8999, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '1TB', 'Interface': 'PCIe Gen4 x4 NVMe', 'Sequential Read': '7300 MB/s', 'Sequential Write': '6300 MB/s'}),
        ('WD Black SN850X 2TB NVMe', 'Western Digital', 'WD-SN850X2T', '2TB PCIe Gen4 | 7300 MB/s Read', 16499, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '2TB', 'Interface': 'PCIe Gen4 x4 NVMe', 'Sequential Read': '7300 MB/s'}),
        ('WD Blue SN580 1TB NVMe', 'Western Digital', 'WD-SN5801T', '1TB PCIe Gen4 | 4150 MB/s Read', 5999, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '1TB', 'Interface': 'PCIe Gen4 x4 NVMe', 'Sequential Read': '4150 MB/s', 'Sequential Write': '4150 MB/s'}),
        ('Kingston NV2 1TB NVMe', 'Kingston', 'KNG-NV21T', '1TB PCIe Gen4 | 3500 MB/s Read', 4499, 1, 18, '3 Years', 'China', 'ssd', {'Capacity': '1TB', 'Interface': 'PCIe Gen4 x4 NVMe', 'Sequential Read': '3500 MB/s', 'Sequential Write': '2100 MB/s'}),
        ('Crucial P3 1TB NVMe', 'Kingston', 'CRU-P31T', '1TB PCIe Gen3 | 3500 MB/s Read', 4299, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '1TB', 'Interface': 'PCIe Gen3 x4 NVMe', 'Sequential Read': '3500 MB/s', 'Sequential Write': '3000 MB/s'}),
        ('Samsung T7 Portable SSD 1TB', 'Samsung', 'SAM-T71T', '1TB Portable USB 3.2 | 1050 MB/s', 8999, 1, 18, '3 Years', 'China', 'ssd', {'Capacity': '1TB', 'Interface': 'USB 3.2 Gen2', 'Sequential Read': '1050 MB/s', 'Sequential Write': '1000 MB/s', 'Weight': '58g'}),
    ],
    'HDD Drives': [
        ('Seagate Barracuda 2TB', 'Seagate', 'SG-BAR2T', '2TB 7200RPM SATA III | 256MB Cache', 4999, 1, 18, '2 Years', 'China', 'hdd', {'Capacity': '2TB', 'RPM': '7200', 'Interface': 'SATA III 6Gb/s', 'Cache': '256MB'}),
        ('Seagate Barracuda 4TB', 'Seagate', 'SG-BAR4T', '4TB 5400RPM SATA III | 256MB Cache', 8499, 1, 18, '2 Years', 'China', 'hdd', {'Capacity': '4TB', 'RPM': '5400', 'Interface': 'SATA III 6Gb/s', 'Cache': '256MB'}),
        ('WD Blue 1TB', 'Western Digital', 'WD-BLUE1T', '1TB 7200RPM SATA III | 64MB Cache', 3299, 1, 18, '2 Years', 'China', 'hdd', {'Capacity': '1TB', 'RPM': '7200', 'Interface': 'SATA III', 'Cache': '64MB'}),
        ('WD Blue 2TB', 'Western Digital', 'WD-BLUE2T', '2TB 7200RPM SATA III | 256MB Cache', 4799, 1, 18, '2 Years', 'China', 'hdd', {'Capacity': '2TB', 'RPM': '7200', 'Interface': 'SATA III', 'Cache': '256MB'}),
        ('Seagate IronWolf 4TB NAS', 'Seagate', 'SG-IW4T', '4TB NAS 7200RPM | 256MB Cache | CMR', 10999, 1, 18, '3 Years', 'China', 'hdd', {'Capacity': '4TB', 'RPM': '7200', 'Interface': 'SATA III', 'Cache': '256MB', 'Workload': '180 TB/yr'}),
        ('Seagate IronWolf 8TB NAS', 'Seagate', 'SG-IW8T', '8TB NAS 7200RPM | 256MB Cache | CMR', 18999, 1, 18, '3 Years', 'China', 'hdd', {'Capacity': '8TB', 'RPM': '7200', 'Interface': 'SATA III', 'Cache': '256MB'}),
        ('WD Red Plus 4TB NAS', 'Western Digital', 'WD-RP4T', '4TB NAS 5400RPM | 256MB Cache', 10499, 1, 18, '3 Years', 'China', 'hdd', {'Capacity': '4TB', 'RPM': '5400', 'Interface': 'SATA III', 'Cache': '256MB', 'Workload': '180 TB/yr'}),
    ],
    'Wireless Routers': [
        ('TP-Link Archer AX73', 'TP-Link', 'TPL-AX73', 'AX5400 | Wi-Fi 6 | 2.5G Port | MU-MIMO', 6999, 1, 18, '3 Years', 'China', 'router', {'Speed': 'AX5400 (574+4804 Mbps)', 'Bands': 'Dual Band 2.4GHz + 5GHz', 'Ports': '1x 2.5G WAN + 4x Gigabit LAN', 'Features': 'MU-MIMO, Beamforming, HomeCare', 'Antenna': '6x External'}),
        ('TP-Link Archer AX55', 'TP-Link', 'TPL-AX55', 'AX3000 | Wi-Fi 6 | Gigabit', 4499, 1, 18, '3 Years', 'China', 'router', {'Speed': 'AX3000 (574+2402 Mbps)', 'Bands': 'Dual Band', 'Ports': '1x Gigabit WAN + 4x Gigabit LAN', 'Features': 'MU-MIMO, OFDMA'}),
        ('TP-Link Deco XE75 Mesh WiFi 6E', 'TP-Link', 'TPL-DECXE75', 'AXE5400 | Wi-Fi 6E | Mesh | 3-Pack', 19999, 1, 18, '3 Years', 'China', 'router', {'Speed': 'AXE5400', 'Bands': 'Tri-Band 2.4+5+6GHz', 'Coverage': 'Up to 7200 sq ft', 'Pack': '3-Pack', 'Features': 'Mesh, AI-Driven'}),
        ('ASUS RT-AX86U Pro', 'ASUS', 'ASUS-RTAX86U', 'AX5700 | Wi-Fi 6 | Gaming Router', 16999, 1, 18, '3 Years', 'Taiwan', 'router', {'Speed': 'AX5700', 'Bands': 'Dual Band', 'Ports': '1x 2.5G WAN + 4x Gigabit LAN', 'Features': 'Game Boost, AiProtection', 'CPU': '2.0 GHz Quad-Core'}),
        ('Cisco RV340 Router', 'Cisco', 'CISCO-RV340', 'Dual WAN | VPN | 4-Port Gigabit | Business', 24999, 1, 18, 'Limited Lifetime', 'China', 'router', {'Ports': '4x Gigabit LAN + 2x Gigabit WAN', 'VPN': 'IPsec, PPTP, L2TP', 'Throughput': '950 Mbps', 'Users': 'Up to 50'}),
    ],
    'Network Switches': [
        ('TP-Link TL-SG1024DE 24-Port', 'TP-Link', 'TPL-SG1024DE', '24-Port Gigabit Easy Smart | QoS | VLAN', 8499, 1, 18, '3 Years', 'China', 'switch', {'Ports': '24 x Gigabit', 'Switching Capacity': '48 Gbps', 'Features': 'QoS, VLAN, IGMP Snooping', 'Management': 'Web-based'}),
        ('TP-Link TL-SG1008PE 8-Port PoE', 'TP-Link', 'TPL-SG1008PE', '8-Port Gigabit PoE | 64W Budget', 5499, 1, 18, '3 Years', 'China', 'switch', {'Ports': '8 x Gigabit PoE', 'PoE Budget': '64W', 'Switching Capacity': '16 Gbps'}),
        ('Cisco Catalyst C1000-24T-4G-L', 'Cisco', 'CISCO-C100024T', '24-Port Gigabit Managed | L2+', 42999, 1, 18, 'Limited Lifetime', 'China', 'switch', {'Ports': '24 x Gigabit + 4x 1G SFP', 'Switching Capacity': '56 Gbps', 'Management': 'Full L2+', 'Features': 'ACL, QoS, SNMP'}),
        ('Cisco Catalyst C9200L-24P-4G-E', 'Cisco', 'CISCO-C9200L24P', '24-Port PoE+ | Managed | Stackable', 145999, 1, 18, 'Limited Lifetime', 'China', 'switch', {'Ports': '24 x 1G PoE+ + 4x 1G SFP', 'PoE Budget': '370W', 'Switching Capacity': '128 Gbps'}),
        ('D-Link DGS-1100-24 24-Port', 'D-Link', 'DL-DGS110024', '24-Port Gigabit Smart Managed', 7499, 1, 18, 'Limited Lifetime', 'Taiwan', 'switch', {'Ports': '24 x Gigabit', 'Switching Capacity': '48 Gbps', 'Management': 'Smart Managed'}),
    ],
    'Access Points': [
        ('TP-Link EAP670 WiFi 6 Access Point', 'TP-Link', 'TPL-EAP670', 'AX5400 | Ceiling Mount | PoE | MU-MIMO', 9999, 1, 18, '5 Years', 'China', 'access_point', {'Speed': 'AX5400', 'Bands': 'Dual Band', 'PoE': '802.3at', 'Coverage': '115 sqm', 'Mounting': 'Ceiling/Wall'}),
        ('TP-Link EAP660 HD WiFi 6 AP', 'TP-Link', 'TPL-EAP660HD', 'AX3600 | High Density | PoE', 12999, 1, 18, '5 Years', 'China', 'access_point', {'Speed': 'AX3600', 'Bands': 'Dual Band', 'PoE': '802.3at', 'Clients': 'Up to 500+'}),
        ('Cisco Business CBS350-8P PoE Switch+AP', 'Cisco', 'CISCO-CBS3508P', '8-Port PoE+ Managed | L2', 19999, 1, 18, 'Limited Lifetime', 'China', 'switch', {'Ports': '8 x 1G PoE+ + 2x 1G SFP', 'PoE Budget': '67W'}),
    ],
    'Firewalls': [
        ('Cisco Firepower 1010 Security Appliance', 'Cisco', 'CISCO-FP1010', 'Next-Gen Firewall | 1Gbps | 10 VPN Peers', 49999, 1, 18, '1 Year', 'China', 'firewall', {'Throughput': '1 Gbps', 'VPN Peers': '10', 'Interfaces': '8x GE', 'Features': 'IPS, URL Filtering, AMP'}),
        ('FortiGate 60F Firewall', 'Cisco', 'FGT-60F', 'Next-Gen Firewall | 10Gbps | Enterprise', 42999, 1, 18, '1 Year', 'China', 'firewall', {'Throughput': '10 Gbps', 'Interfaces': '10x GE', 'Features': 'NGFW, IPS, SSL Inspection'}),
    ],
    'Mice': [
        ('Logitech MX Master 3S Mouse', 'Logitech', 'LOG-MXM3S', 'Wireless | 8K DPI | USB-C | Quiet Click', 8999, 1, 18, '1 Year', 'China', 'mouse', {'DPI': '8000', 'Connectivity': 'Bluetooth + Unifying', 'Buttons': '7', 'Battery': '70 days', 'Weight': '141g'}),
        ('Logitech MX Ergo Trackball', 'Logitech', 'LOG-MXERG', 'Wireless Trackball | 2000 DPI', 7999, 1, 18, '1 Year', 'China', 'mouse', {'DPI': '2000', 'Connectivity': 'Bluetooth + USB', 'Type': 'Trackball', 'Battery': '4 months'}),
        ('Logitech G502 X Plus Gaming', 'Logitech', 'LOG-G502XP', 'Wireless | 25600 DPI | LIGHTFORCE', 12999, 1, 18, '2 Years', 'China', 'mouse', {'DPI': '25600', 'Connectivity': 'LIGHTSPEED Wireless', 'Buttons': '13', 'Weight': '106g'}),
        ('Logitech M240 Silent', 'Logitech', 'LOG-M240', 'Wireless | 1000 DPI | Silent Click', 1299, 1, 18, '1 Year', 'China', 'mouse', {'DPI': '1000', 'Connectivity': 'Bluetooth', 'Buttons': '3', 'Battery': '24 months'}),
        ('Razer DeathAdder V3 Gaming', 'Razer', 'RAZ-DAV3', 'Wired | 30000 DPI | 63g Ultralight', 5999, 1, 18, '2 Years', 'China', 'mouse', {'DPI': '30000', 'Connectivity': 'USB-C', 'Buttons': '5', 'Weight': '63g'}),
        ('Razer Viper V2 Pro', 'Razer', 'RAZ-VV2P', 'Wireless | 30000 DPI | 58g', 14999, 1, 18, '2 Years', 'China', 'mouse', {'DPI': '30000', 'Connectivity': 'HyperSpeed Wireless', 'Weight': '58g', 'Battery': '80 hours'}),
        ('Zebronics Zeb-Transformer Gaming', 'Zebronics', 'ZEB-TRANS', 'Wired | 4800 DPI | RGB | Gaming', 799, 2, 18, '1 Year', 'India', 'mouse', {'DPI': '4800', 'Connectivity': 'USB', 'Buttons': '6', 'RGB': 'Yes'}),
    ],
    'Keyboards': [
        ('Logitech MX Keys S Wireless', 'Logitech', 'LOG-MXKEYS', 'Wireless | Backlit | Smart Actions', 9999, 1, 18, '1 Year', 'China', 'keyboard', {'Type': 'Low Profile', 'Connectivity': 'Bluetooth + USB-C', 'Backlight': 'Yes - Adaptive', 'Battery': '10 days'}),
        ('Logitech MX Mechanical', 'Logitech', 'LOG-MXMECH', 'Wireless | Mechanical | Backlit', 13999, 1, 18, '1 Year', 'China', 'keyboard', {'Type': 'Mechanical', 'Switch': 'Tactile Quiet', 'Connectivity': 'Bluetooth + USB-C', 'Backlight': 'Yes'}),
        ('Corsair K100 RGB Mechanical', 'Corsair', 'COR-K100', 'Wired | Cherry MX Speed | RGB | iCUE', 16999, 1, 18, '2 Years', 'China', 'keyboard', {'Type': 'Mechanical', 'Switch': 'Cherry MX Speed', 'Backlight': 'RGB Per-Key', 'Features': 'iCUE Control Wheel'}),
        ('Corsair K65 Plus Wireless', 'Corsair', 'COR-K65PW', 'Wireless | 75% | Hot-Swap | RGB', 12999, 1, 18, '2 Years', 'China', 'keyboard', {'Type': 'Mechanical 75%', 'Connectivity': 'Wireless', 'Hot-Swap': 'Yes', 'Battery': '266 hours'}),
        ('Razer BlackWidow V4 75%', 'Razer', 'RAZ-BWV475', 'Wired | Hot-Swap | Optical | RGB', 14999, 1, 18, '2 Years', 'China', 'keyboard', {'Type': 'Mechanical 75%', 'Switch': 'Razer Orange Optical', 'Hot-Swap': 'Yes', 'Backlight': 'RGB'}),
        ('Zebronics Zeb-MK1000 Multimedia', 'Zebronics', 'ZEB-MK1000', 'Wired | Multimedia Keys | USB', 599, 2, 18, '1 Year', 'India', 'keyboard', {'Type': 'Membrane', 'Connectivity': 'USB', 'Keys': '104', 'Features': 'Multimedia Keys'}),
        ('HP K200 USB Keyboard', 'HP', 'HP-K200', 'Wired | Full Size | USB | Spill Resistant', 699, 2, 18, '1 Year', 'China', 'keyboard', {'Type': 'Membrane', 'Connectivity': 'USB', 'Keys': '104', 'Features': 'Spill Resistant'}),
    ],
    'Webcams': [
        ('Logitech C920s HD Pro Webcam', 'Logitech', 'LOG-C920S', '1080p | Auto Light Correction | Privacy Shield', 5499, 1, 18, '1 Year', 'China', 'webcam', {'Resolution': '1080p @ 30fps', 'FOV': '78 degrees', 'Microphone': 'Dual Stereo', 'Features': 'Privacy Shield, Auto Light Correct'}),
        ('Logitech Brio 4K Webcam', 'Logitech', 'LOG-BRIO', '4K UHD | HDR | Windows Hello', 16999, 1, 18, '1 Year', 'China', 'webcam', {'Resolution': '4K @ 30fps / 1080p @ 60fps', 'FOV': '90/78/65 degrees', 'HDR': 'Yes', 'Features': 'Windows Hello, Noise Cancellation'}),
        ('Logitech Rally Bar Mini', 'Logitech', 'LOG-RBM', 'Video Bar | 4K | AI Auto-Frame', 189999, 1, 18, '2 Years', 'China', 'webcam', {'Resolution': '4K', 'Camera': 'Dual Camera', 'Microphone': '6-mic Beamforming', 'Speakers': 'Integrated', 'AI': 'Auto-Frame, Noise Suppression'}),
    ],
    'Headphones': [
        ('Sony WH-1000XM5', 'Sony', 'SONY-WH1000XM5', 'Wireless ANC | 30hr Battery | Hi-Res', 29990, 1, 18, '1 Year', 'Malaysia', 'headphones', {'Type': 'Over-Ear Wireless', 'ANC': 'Industry Leading', 'Battery': '30 hours', 'Driver': '30mm', 'Weight': '250g', 'Codec': 'LDAC, AAC, SBC'}),
        ('Sony WH-1000XM4', 'Sony', 'SONY-WH1000XM4', 'Wireless ANC | 30hr Battery | Hi-Res', 22990, 1, 18, '1 Year', 'Malaysia', 'headphones', {'Type': 'Over-Ear Wireless', 'ANC': 'Yes', 'Battery': '30 hours', 'Driver': '40mm', 'Weight': '254g'}),
        ('Sony WF-1000XM5 TWS', 'Sony', 'SONY-WF1000XM5', 'True Wireless ANC | 8hr + 16hr Case', 24990, 1, 18, '1 Year', 'China', 'earbuds', {'Type': 'True Wireless', 'ANC': 'Industry Leading', 'Battery': '8hr + 16hr', 'Driver': '8.4mm Dynamic', 'Codec': 'LDAC, AAC'}),
        ('Bose QuietComfort Ultra', 'Bose', 'BOSE-QCULTRA', 'Wireless ANC | Immersive Audio | 24hr', 34999, 1, 18, '1 Year', 'China', 'headphones', {'Type': 'Over-Ear Wireless', 'ANC': 'CustomTune', 'Battery': '24 hours', 'Audio': 'Immersive Spatial Audio'}),
        ('JBL Tune 770NC', 'JBL', 'JBL-770NC', 'Wireless ANC | 70hr Battery | Hi-Res', 7999, 1, 18, '1 Year', 'China', 'headphones', {'Type': 'Over-Ear Wireless', 'ANC': 'Adaptive', 'Battery': '70 hours', 'Driver': '40mm'}),
        ('JBL Live Pro 2 TWS', 'JBL', 'JBL-LPP2', 'True Wireless | ANC | 40hr Total', 9999, 1, 18, '1 Year', 'China', 'earbuds', {'Type': 'True Wireless', 'ANC': 'Yes', 'Battery': '10hr + 30hr', 'Driver': '10mm'}),
        ('Razer BlackShark V2 Pro', 'Razer', 'RAZ-BSV2P', 'Wireless Gaming | THX Spatial | 70hr', 16999, 1, 18, '2 Years', 'China', 'headphones', {'Type': 'Over-Ear Wireless', 'Driver': '50mm Titanium', 'Battery': '70 hours', 'Audio': 'THX Spatial Audio'}),
    ],
    'Speakers': [
        ('JBL Charge 5', 'JBL', 'JBL-CHG5', 'Portable Bluetooth | IP67 | 20hr | Powerbank', 17999, 1, 18, '1 Year', 'China', 'speaker', {'Type': 'Portable Bluetooth', 'Waterproof': 'IP67', 'Battery': '20 hours', 'Output': '30W', 'Features': 'Powerbank function'}),
        ('JBL Flip 6', 'JBL', 'JBL-FLIP6', 'Portable Bluetooth | IP67 | 12hr', 12999, 1, 18, '1 Year', 'China', 'speaker', {'Type': 'Portable Bluetooth', 'Waterproof': 'IP67', 'Battery': '12 hours', 'Output': '20W'}),
        ('Sony SRS-XB100', 'Sony', 'SONY-XB100', 'Portable Bluetooth | IP67 | 16hr', 4999, 1, 18, '1 Year', 'China', 'speaker', {'Type': 'Portable Bluetooth', 'Waterproof': 'IP67', 'Battery': '16 hours', 'Weight': '274g'}),
        ('Bose SoundLink Flex', 'Bose', 'BOSE-SLF', 'Portable Bluetooth | IP67 | PositionIQ', 14999, 1, 18, '1 Year', 'China', 'speaker', {'Type': 'Portable Bluetooth', 'Waterproof': 'IP67', 'Battery': '12 hours', 'Features': 'PositionIQ'}),
        ('Logitech Z313 2.1 Speaker', 'Logitech', 'LOG-Z313', '2.1 Channel | 50W | Wired Subwoofer', 3999, 1, 18, '1 Year', 'China', 'speaker', {'Type': '2.1 Desktop', 'Power': '50W', 'Subwoofer': 'Wired', 'Control': 'Wired Remote'}),
        ('Bose Solo 5 Soundbar', 'Bose', 'BOSS-SOLO5', 'Bluetooth Soundbar | Dialogue Mode', 19999, 1, 18, '1 Year', 'China', 'speaker', {'Type': 'Soundbar', 'Connectivity': 'Bluetooth, Optical, Coax', 'Features': 'Dialogue Mode'}),
    ],
    'Earbuds': [
        ('Samsung Galaxy Buds2 Pro', 'Samsung', 'SAM-GB2PRO', 'True Wireless ANC | 24bit Audio | IPX7', 12999, 1, 18, '1 Year', 'Vietnam', 'earbuds', {'Type': 'True Wireless', 'ANC': 'Intelligent ANC', 'Battery': '5hr + 18hr', 'Audio': '24bit Hi-Fi', 'Waterproof': 'IPX7'}),
        ('Apple AirPods Pro 2', 'Apple', 'APL-APP2', 'True Wireless ANC | Adaptive Audio | IP54', 24900, 1, 18, '1 Year', 'China', 'earbuds', {'Type': 'True Wireless', 'ANC': 'Active + Transparency', 'Battery': '6hr + 30hr', 'Chip': 'H2', 'Features': 'Adaptive Audio, Personalized Spatial'}),
        ('JBL Tune Buds', 'JBL', 'JBL-TBUDS', 'True Wireless ANC | 48hr Total | IP54', 5999, 1, 18, '1 Year', 'China', 'earbuds', {'Type': 'True Wireless', 'ANC': 'Yes', 'Battery': '12hr + 36hr', 'Driver': '10mm'}),
        ('OnePlus Buds Pro 2', 'Samsung', 'OP-BP2', 'True Wireless ANC | LDAC | 39hr Total', 9999, 1, 18, '1 Year', 'China', 'earbuds', {'Type': 'True Wireless', 'ANC': 'Smart ANC', 'Battery': '6hr + 33hr', 'Codec': 'LDAC, AAC'}),
        ('Zebronics Zeb Pods Pro', 'Zebronics', 'ZEB-PODSP', 'True Wireless | ANC | 42hr Total', 2499, 2, 18, '1 Year', 'India', 'earbuds', {'Type': 'True Wireless', 'ANC': 'Hybrid ANC', 'Battery': '7hr + 35hr', 'Driver': '13mm'}),
    ],
    'Microphones': [
        ('Blue Yeti X USB Mic', 'Logitech', 'BLUE-YETIX', 'USB Condenser | 4 Patterns | LED Meter', 14999, 1, 18, '2 Years', 'China', 'microphone', {'Type': 'USB Condenser', 'Patterns': '4 (Cardioid, Bidirectional, Omni, Stereo)', 'Sample Rate': '48kHz', 'Bit Depth': '24-bit', 'LED': 'Yes'}),
        ('Rode NT1 5th Gen', 'Logitech', 'RODE-NT1G5', 'XLR/USB Condenser | Ultra-Low Noise', 19999, 1, 18, '1 Year', 'Australia', 'microphone', {'Type': 'Condenser', 'Patterns': 'Cardioid', 'Noise': '4dBA', 'Connector': 'XLR + USB-C', 'Sample Rate': '192kHz'}),
        ('Samson Q2U Dynamic Mic', 'Logitech', 'SAM-Q2U', 'Dynamic | XLR/USB | Broadcast', 5999, 1, 18, '1 Year', 'China', 'microphone', {'Type': 'Dynamic', 'Patterns': 'Cardioid', 'Connector': 'XLR + USB'}),
    ],
    'Monitors': [
        ('Dell UltraSharp U2723QE 27" 4K', 'Dell', 'DELL-U2723QE', '27" 4K UHD | IPS Black | USB-C Hub | 98% DCI-P3', 49999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '27 inch', 'Resolution': '3840x2160', 'Panel': 'IPS Black', 'Color': '98% DCI-P3, 100% sRGB', 'Connectivity': 'USB-C 90W, HDMI, DP', 'Refresh': '60Hz'}),
        ('Dell P2723QE 27" 4K USB-C', 'Dell', 'DELL-P2723QE', '27" 4K UHD | IPS | USB-C 90W', 37999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '27 inch', 'Resolution': '3840x2160', 'Panel': 'IPS', 'Connectivity': 'USB-C 90W, HDMI, DP'}),
        ('HP E24m G4 24" FHD USB-C', 'HP', 'HP-E24MG4', '24" FHD | IPS | USB-C | Pop-Up Webcam', 22999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '24 inch', 'Resolution': '1920x1080', 'Panel': 'IPS', 'Connectivity': 'USB-C 65W, HDMI, DP', 'Webcam': 'Pop-Up 5MP'}),
        ('Samsung Odyssey G5 27" QHD 165Hz', 'Samsung', 'SAM-ODG527', '27" QHD | VA | 165Hz | 1ms | Curved 1000R', 24999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '27 inch', 'Resolution': '2560x1440', 'Panel': 'VA Curved 1000R', 'Refresh': '165Hz', 'Response': '1ms MPRT', 'HDR': 'HDR10'}),
        ('Samsung Odyssey G7 32" QHD 240Hz', 'Samsung', 'SAM-ODG732', '32" QHD | VA | 240Hz | 1ms | Curved 1000R', 39999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '32 inch', 'Resolution': '2560x1440', 'Panel': 'VA Curved 1000R', 'Refresh': '240Hz', 'Response': '1ms'}),
        ('LG 27GP850-B 27" QHD Nano IPS', 'Samsung', 'LG-27GP850', '27" QHD | Nano IPS | 165Hz (OC 180Hz)', 32999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '27 inch', 'Resolution': '2560x1440', 'Panel': 'Nano IPS', 'Refresh': '165Hz (180Hz OC)', 'HDR': 'HDR400', 'Color': '98% DCI-P3'}),
        ('ASUS ProArt PA279CRV 27" 4K', 'ASUS', 'ASUS-PA279CRV', '27" 4K | IPS | 99% DCI-P3 | Calman Verified', 54999, 1, 18, '3 Years', 'Taiwan', 'monitor', {'Size': '27 inch', 'Resolution': '3840x2160', 'Panel': 'IPS', 'Color': '99% DCI-P3', 'Features': 'Calman Verified, USB-C 96W'}),
        ('Dell P2422H 24" FHD', 'Dell', 'DELL-P2422H', '24" FHD | IPS | Height Adjust', 16999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '24 inch', 'Resolution': '1920x1080', 'Panel': 'IPS', 'Ergonomics': 'Height, Tilt, Swivel, Pivot'}),
        ('Lenovo ThinkVision T24i-30 24" FHD', 'Lenovo', 'LEN-T24I30', '24" FHD | IPS | USB-C | NearEdgeless', 15999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '24 inch', 'Resolution': '1920x1080', 'Panel': 'IPS', 'Connectivity': 'USB-C 75W, HDMI, DP'}),
        ('HP Z32 32" 4K USB-C', 'HP', 'HP-Z32', '32" 4K UHD | IPS | USB-C | DreamColor', 64999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '32 inch', 'Resolution': '3840x2160', 'Panel': 'IPS', 'Color': '99% sRGB, DreamColor'}),
    ],
    'Printers': [
        ('HP LaserJet Pro M404dn', 'HP', 'HP-LJM404DN', 'Mono Laser | Duplex | Ethernet | 38ppm', 29999, 1, 18, '1 Year', 'China', 'printer', {'Type': 'Mono Laser', 'Speed': '38 ppm', 'Resolution': '4800x600 dpi', 'Duplex': 'Auto', 'Connectivity': 'Ethernet, USB', 'Paper': 'Up to A4'}),
        ('HP LaserJet Pro MFP M428fdw', 'HP', 'HP-LJM428FDW', 'Mono Laser MFP | Print/Copy/Scan/Fax | Duplex', 42999, 1, 18, '1 Year', 'China', 'printer', {'Type': 'Mono Laser MFP', 'Speed': '40 ppm', 'Functions': 'Print, Copy, Scan, Fax', 'Duplex': 'Auto', 'Connectivity': 'WiFi, Ethernet, USB'}),
        ('HP Color LaserJet Pro MFP M283fdw', 'HP', 'HP-CLJM283', 'Color Laser MFP | Print/Copy/Scan/Fax | Duplex', 54999, 1, 18, '1 Year', 'China', 'printer', {'Type': 'Color Laser MFP', 'Speed': '24 ppm', 'Functions': 'Print, Copy, Scan, Fax', 'Duplex': 'Auto', 'Connectivity': 'WiFi, Ethernet'}),
        ('Epson EcoTank L3250 Ink Tank', 'Epson', 'EP-L3250', 'Color Ink Tank | WiFi | Print/Copy/Scan', 15999, 1, 18, '1 Year or 30K pages', 'Indonesia', 'printer', {'Type': 'Ink Tank', 'Speed': '33 ppm (Black)', 'Functions': 'Print, Copy, Scan', 'Connectivity': 'WiFi, USB', 'Page Yield': '4500 Black / 7500 Color'}),
        ('Epson EcoTank L6270 Ink Tank', 'Epson', 'EP-L6270', 'Color Ink Tank | Duplex | ADF | WiFi', 26999, 1, 18, '1 Year or 50K pages', 'Indonesia', 'printer', {'Type': 'Color Ink Tank MFP', 'Speed': '33 ppm', 'Functions': 'Print, Copy, Scan, Fax', 'ADF': '30 sheets', 'Duplex': 'Auto'}),
        ('Brother HL-L2370DW Mono Laser', 'Brother', 'BRO-HLL2370DW', 'Mono Laser | Duplex | WiFi | 34ppm', 18999, 1, 18, '3 Years', 'China', 'printer', {'Type': 'Mono Laser', 'Speed': '34 ppm', 'Duplex': 'Auto', 'Connectivity': 'WiFi, Ethernet, USB'}),
        ('Brother DCP-L2541DW Mono Laser MFP', 'Brother', 'BRO-DCPL2541', 'Mono Laser MFP | Print/Copy/Scan | Duplex | ADF', 22999, 1, 18, '3 Years', 'China', 'printer', {'Type': 'Mono Laser MFP', 'Speed': '30 ppm', 'Functions': 'Print, Copy, Scan', 'ADF': '35 sheets', 'Duplex': 'Auto'}),
        ('HP LaserJet M1005 Mono', 'HP', 'HP-LJM1005', 'Mono Laser | USB | 14ppm', 13999, 1, 18, '1 Year', 'China', 'printer', {'Type': 'Mono Laser', 'Speed': '14 ppm', 'Resolution': '600x600 dpi', 'Connectivity': 'USB'}),
        ('Epson TM-T88VII POS Receipt', 'Epson', 'EP-TMT88VII', 'POS Thermal Receipt | Ethernet | USB', 22999, 1, 18, '4 Years', 'China', 'printer', {'Type': 'Thermal Receipt', 'Speed': '500 mm/s', 'Connectivity': 'Ethernet, USB, Serial', 'Auto-Cutter': 'Yes'}),
        ('Zebra ZD421t Direct Thermal', 'Zebronics', 'ZEB-ZD421T', 'Label Printer | 203dpi | USB+Ethernet', 19999, 1, 18, '2 Years', 'China', 'printer', {'Type': 'Label Printer', 'Resolution': '203 dpi', 'Print Width': '4.09 inch', 'Speed': '10 ips', 'Connectivity': 'USB, Ethernet'}),
    ],
    'Barcode Scanners': [
        ('Honeywell Voyager 1200g', 'Honeywell', 'HON-V1200G', 'Single-Line Laser Scanner | USB', 7999, 1, 18, '5 Years', 'China', 'scan', {'Type': 'Laser Scanner', 'Interface': 'USB', 'Scan Rate': '100 scans/sec', 'Depth': '0 - 17 inches'}),
        ('Honeywell Xenon 1900gHD', 'Honeywell', 'HON-XEN1900', 'Area-Imaging Scanner | 1D/2D | USB', 19999, 1, 18, '5 Years', 'China', 'scan', {'Type': 'Area-Imaging', 'Interface': 'USB', 'Scan Rate': '100 scans/sec', 'Decode': '1D, 2D, PDF'}),
        ('Zebra DS2208 2D Scanner', 'Zebronics', 'ZEB-DS2208', '2D Imager | USB | Handheld', 8999, 1, 18, '5 Years', 'China', 'scan', {'Type': '2D Imager', 'Interface': 'USB', 'Scan Rate': '100 scans/sec'}),
    ],
    'CCTV Cameras': [
        ('Hikvision DS-2CD2T47 4MP Bullet', 'Hikvision', 'HIK-2CD2T47', '4MP | ColorVu | 40m IR | IP67', 5999, 2, 18, '3 Years', 'China', 'cctv', {'Resolution': '4MP (2560x1440)', 'Lens': '4mm', 'IR Range': '40m', 'Features': 'ColorVu, Smart Detection', 'Rating': 'IP67'}),
        ('Hikvision DS-2CD2347 4MP Turret', 'Hikvision', 'HIK-2CD2347', '4MP | ColorVu | 30m IR | IP67', 5499, 2, 18, '3 Years', 'China', 'cctv', {'Resolution': '4MP', 'Lens': '4mm', 'IR Range': '30m', 'Features': 'ColorVu, AcuSense', 'Rating': 'IP67'}),
        ('Hikvision DS-2DE4A425IWG-E 4MP PTZ', 'Hikvision', 'HIK-2DE4A', '4MP | 25x Zoom | PTZ | IR 100m', 32999, 1, 18, '3 Years', 'China', 'cctv', {'Resolution': '4MP', 'Zoom': '25x Optical', 'IR Range': '100m', 'PTZ': 'Pan/Tilt/Zoom', 'Features': 'Smart Tracking'}),
        ('CP Plus 2MP Bullet Camera', 'CP Plus', 'CP-2MPBUL', '2MP | 20m IR | IP66 | CMOS', 2499, 2, 18, '2 Years', 'India', 'cctv', {'Resolution': '2MP (1920x1080)', 'Lens': '3.6mm', 'IR Range': '20m', 'Rating': 'IP66'}),
        ('CP Plus 4MP Dome Camera', 'CP Plus', 'CP-4MPDOME', '4MP | 30m IR | IP67 | WDR', 3999, 2, 18, '2 Years', 'India', 'cctv', {'Resolution': '4MP', 'Lens': '2.8mm', 'IR Range': '30m', 'Features': 'WDR, Smart IR', 'Rating': 'IP67'}),
        ('Hikvision DS-7600NI-K2/4P NVR', 'Hikvision', 'HIK-7600NI', '8-Ch Network Video Recorder | 4K | PoE', 18999, 1, 18, '3 Years', 'China', 'cctv', {'Channels': '8', 'Resolution': 'Up to 4K', 'PoE': '4 Ports', 'Storage': 'Up to 10TB HDD', 'Features': 'H.265+, Smart Playback'}),
        ('CP Plus 16-Ch NVR', 'CP Plus', 'CP-16CHNVR', '16-Ch Network Video Recorder | 4K | PoE', 16999, 1, 18, '2 Years', 'India', 'cctv', {'Channels': '16', 'Resolution': 'Up to 4K', 'PoE': '16 Ports', 'Storage': 'Up to 20TB'}),
    ],
    'UPS Systems': [
        ('APC Back-UPS BX1100LI-IN 1100VA', 'APC', 'APC-BX1100', '1100VA / 660W | Line-Interactive | 2 Outlets', 8499, 1, 18, '2 Years', 'China', 'ups', {'Capacity': '1100VA / 660W', 'Type': 'Line-Interactive', 'Outlets': 'Indian 3-pin', 'Battery': 'Sealed Lead-Acid', 'Runtime': '~30 min at half load'}),
        ('APC Back-UPS BX1500MI-IN 1500VA', 'APC', 'APC-BX1500', '1500VA / 900W | Line-Interactive', 12999, 1, 18, '2 Years', 'China', 'ups', {'Capacity': '1500VA / 900W', 'Type': 'Line-Interactive', 'Outlets': 'Indian 3-pin + USB'}),
        ('APC Smart-UPS SMT1000IC 1000VA', 'APC', 'APC-SMT1000', '1000VA / 700W | Online | SmartConnect', 32999, 1, 18, '3 Years', 'China', 'ups', {'Capacity': '1000VA / 700W', 'Type': 'Line-Interactive', 'Features': 'SmartConnect Cloud, AVR', 'Outlets': '6'}),
        ('APC Smart-UPS SMT2200IC 2200VA', 'APC', 'APC-SMT2200', '2200VA / 1920W | Line-Interactive | SmartConnect', 64999, 1, 18, '3 Years', 'China', 'ups', {'Capacity': '2200VA / 1920W', 'Type': 'Line-Interactive', 'Features': 'SmartConnect, LCD Display'}),
        ('APC Symmetra LX 4kVA Module', 'APC', 'APC-SYMLX4', '4kVA Scalable UPS | Redundant | Hot-Swappable', 199999, 1, 18, '1 Year', 'China', 'ups', {'Capacity': '4kVA / 3.6kW', 'Type': 'Modular', 'Features': 'Hot-Swappable, Redundant', 'Scalable': 'Up to 8kVA'}),
        ('Luminous Zelio 1100VA Home UPS', 'APC', 'LUM-ZELIO', '1100VA / 756W | Home UPS | Intelligent Load Management', 6499, 1, 18, '2 Years', 'India', 'ups', {'Capacity': '1100VA / 756W', 'Type': 'Home UPS', 'Features': 'Intelligent Load Management, LED Display'}),
    ],
    'Inverters': [
        ('Luminous Eco Volt Neo 1050VA', 'APC', 'LUM-ECOV1050', '1050VA / 750W | Pure Sine Wave | 1 Battery', 7999, 1, 18, '2 Years', 'India', 'inverter', {'Capacity': '1050VA / 750W', 'Wave': 'Pure Sine Wave', 'Batteries': '1 x 12V', 'Load': 'Up to 750W'}),
        ('Microtek EM4160+ 1500VA', 'APC', 'MIC-EM4160', '1500VA / 1200W | Digital Display', 10999, 1, 18, '2 Years', 'India', 'inverter', {'Capacity': '1500VA / 1200W', 'Wave': 'Pure Sine Wave', 'Batteries': '1-2 x 12V'}),
        ('APC Home UPS 1500VA', 'APC', 'APC-HOME1500', '1500VA / 1050W | Bypass Switch', 11999, 1, 18, '2 Years', 'China', 'inverter', {'Capacity': '1500VA / 1050W', 'Type': 'Home UPS', 'Features': 'Bypass Switch, MCB Protection'}),
    ],
    'Smartphones': [
        ('Samsung Galaxy S24 Ultra', 'Samsung', 'SAM-S24U256', '6.8" AMOLED | SD 8 Gen 3 | 12GB | 256GB | S Pen', 129999, 1, 18, '1 Year', 'India', 'smartphone', {'Display': '6.8" Dynamic AMOLED 2X', 'Processor': 'Snapdragon 8 Gen 3', 'RAM': '12GB', 'Storage': '256GB', 'Camera': '200MP + 50MP + 12MP + 10MP', 'Battery': '5000mAh'}),
        ('Samsung Galaxy S24+', 'Samsung', 'SAM-S24P256', '6.7" AMOLED | SD 8 Gen 3 | 12GB | 256GB', 94999, 1, 18, '1 Year', 'India', 'smartphone', {'Display': '6.7" Dynamic AMOLED 2X', 'Processor': 'Snapdragon 8 Gen 3', 'RAM': '12GB', 'Storage': '256GB', 'Camera': '50MP + 12MP + 10MP'}),
        ('Samsung Galaxy A55 5G', 'Samsung', 'SAM-A55128', '6.6" AMOLED | Exynos 1480 | 8GB | 128GB', 39999, 1, 18, '1 Year', 'India', 'smartphone', {'Display': '6.6" Super AMOLED 120Hz', 'Processor': 'Exynos 1480', 'RAM': '8GB', 'Storage': '128GB', 'Camera': '50MP + 12MP + 5MP', 'Battery': '5000mAh'}),
        ('Apple iPhone 15 Pro Max', 'Apple', 'APL-IP15PM256', '6.7" XDR | A17 Pro | 256GB | Titanium', 159900, 1, 18, '1 Year', 'China', 'smartphone', {'Display': '6.7" Super Retina XDR', 'Processor': 'A17 Pro', 'Storage': '256GB', 'Camera': '48MP + 12MP + 12MP', 'Material': 'Titanium'}),
        ('Apple iPhone 15', 'Apple', 'APL-IP15128', '6.1" XDR | A16 | 128GB', 79900, 1, 18, '1 Year', 'China', 'smartphone', {'Display': '6.1" Super Retina XDR', 'Processor': 'A16 Bionic', 'Storage': '128GB', 'Camera': '48MP + 12MP'}),
        ('OnePlus 12 5G', 'Samsung', 'OP12-256', '6.82" AMOLED | SD 8 Gen 3 | 16GB | 256GB', 64999, 1, 18, '1 Year', 'China', 'smartphone', {'Display': '6.82" LTPO AMOLED 120Hz', 'Processor': 'Snapdragon 8 Gen 3', 'RAM': '16GB', 'Storage': '256GB', 'Camera': '50MP + 48MP + 64MP', 'Battery': '5400mAh'}),
    ],
    'Power Banks': [
        ('Samsung 10000mAh Wireless Power Bank', 'Samsung', 'SAM-PB10W', '10000mAh | 15W Wireless | USB-C PD', 3999, 1, 18, '1 Year', 'China', 'powerbank', {'Capacity': '10000mAh', 'Output': '15W Wireless + 25W USB-C', 'Input': '25W USB-C', 'Weight': '230g'}),
        ('Mi Power Bank 4 20000mAh', 'Samsung', 'MI-PB420K', '20000mAh | 18W Fast Charge | Dual USB', 1999, 1, 18, '6 Months', 'China', 'powerbank', {'Capacity': '20000mAh', 'Output': '18W Dual USB', 'Input': '18W USB-C', 'Weight': '446g'}),
        ('Baseus 20000mAh 65W PD Power Bank', 'Samsung', 'BAS-65W20K', '20000mAh | 65W PD | Laptop Charging', 4999, 1, 18, '1 Year', 'China', 'powerbank', {'Capacity': '20000mAh / 72Wh', 'Output': '65W USB-C + 22.5W USB-A', 'Features': 'Laptop Charging, LED Display'}),
    ],
    'Chargers': [
        ('Samsung 25W USB-C Super Fast Charger', 'Samsung', 'SAM-25WCHG', '25W | USB-C PD 3.0 | GaN', 1799, 1, 18, '1 Year', 'Vietnam', 'charger', {'Power': '25W', 'Port': 'USB-C PD 3.0', 'Technology': 'GaN', 'Weight': '53g'}),
        ('Apple 20W USB-C Power Adapter', 'Apple', 'APL-20WCHG', '20W | USB-C PD | Fast Charge', 1900, 1, 18, '1 Year', 'China', 'charger', {'Power': '20W', 'Port': 'USB-C PD'}),
        ('Anker Nano II 65W GaN Charger', 'Samsung', 'ANK-N65W', '65W | USB-C PD | GaN II | 3-Port', 4499, 1, 18, '18 Months', 'China', 'charger', {'Power': '65W', 'Ports': '2x USB-C + 1x USB-A', 'Technology': 'GaN II', 'Weight': '134g'}),
        ('Belkin 65W USB-C GaN Charger', 'Samsung', 'BLK-65WGAN', '65W | USB-C | GaN | Foldable', 3999, 1, 18, '2 Years', 'China', 'charger', {'Power': '65W', 'Ports': '1x USB-C', 'Technology': 'GaN', 'Features': 'Foldable Prongs'}),
    ],
    'Cables': [
        ('Anker PowerLine III USB-C to C 100W', 'Samsung', 'ANK-USBCC1M', 'USB-C to C | 100W PD | 1m | Nylon', 999, 1, 18, '18 Months', 'China', 'cable', {'Type': 'USB-C to USB-C', 'Power': '100W PD', 'Length': '1m', 'Material': 'Nylon Braided'}),
        ('Anker PowerLine III USB-C to C 2m', 'Samsung', 'ANK-USBCC2M', 'USB-C to C | 100W PD | 2m | Nylon', 1299, 1, 18, '18 Months', 'China', 'cable', {'Type': 'USB-C to USB-C', 'Power': '100W PD', 'Length': '2m', 'Material': 'Nylon Braided'}),
        ('Belkin HDMI 2.1 Ultra High Speed 2m', 'Samsung', 'BLK-HDMI21', 'HDMI 2.1 | 48Gbps | 8K@60Hz | 2m', 1999, 1, 18, '2 Years', 'China', 'cable', {'Type': 'HDMI 2.1', 'Bandwidth': '48Gbps', 'Resolution': '8K@60Hz, 4K@120Hz', 'Length': '2m'}),
        ('Samsung 1.5m USB-C to C Cable', 'Samsung', 'SAM-USBC15', 'USB-C to C | 3A | 1.5m', 699, 1, 18, '1 Year', 'China', 'cable', {'Type': 'USB-C to USB-C', 'Current': '3A', 'Length': '1.5m'}),
    ],
    'Servers': [
        ('Dell PowerEdge R760 Rack Server', 'Dell', 'DELL-R760', '2U | Dual Xeon 4th Gen | 8x DDR5 | 8x NVMe', 349999, 1, 18, '3 Years', 'China', 'server', {'Form Factor': '2U Rack', 'Processor': 'Dual Intel Xeon Scalable 4th Gen', 'Memory': 'Up to 2TB DDR5', 'Storage': '8x NVMe SSD', 'Network': '2x 25GbE SFP28'}),
        ('Dell PowerEdge T360 Tower Server', 'Dell', 'DELL-T360', 'Tower | Xeon E-2400 | 32GB | 2x 1TB SATA', 129999, 1, 18, '3 Years', 'China', 'server', {'Form Factor': 'Tower', 'Processor': 'Intel Xeon E-2400 Series', 'Memory': '32GB DDR5 ECC', 'Storage': '2x 1TB SATA HDD', 'Network': '2x 1GbE'}),
        ('HP ProLiant DL380 Gen11', 'HP', 'HP-DL380G11', '2U | Dual Xeon 4th Gen | 12x DDR5 | 8x SAS/SATA', 399999, 1, 18, '3 Years', 'China', 'server', {'Form Factor': '2U Rack', 'Processor': 'Dual Intel Xeon Scalable 4th Gen', 'Memory': 'Up to 2TB DDR5', 'Storage': '8x SAS/SATA + 6x NVMe'}),
    ],
    'NAS Storage': [
        ('Synology DS923+ 4-Bay NAS', 'Samsung', 'SYN-DS923', '4-Bay | AMD Ryzen R1600 | 4GB DDR4 ECC', 59999, 1, 18, '3 Years', 'China', 'nas', {'Bays': '4', 'Processor': 'AMD Ryzen R1600', 'RAM': '4GB DDR4 ECC (Max 32GB)', 'Network': '2x 1GbE', 'Features': 'Synology DSM, Btrfs, snapshots'}),
        ('Synology DS223 2-Bay NAS', 'Samsung', 'SYN-DS223', '2-Bay | Realtek RTD1619B | 1GB DDR4', 29999, 1, 18, '2 Years', 'China', 'nas', {'Bays': '2', 'Processor': 'Realtek RTD1619B', 'RAM': '1GB DDR4', 'Network': '1x 1GbE'}),
        ('WD My Cloud EX2 Ultra 8TB', 'Western Digital', 'WD-EX2U8T', '2-Bay NAS | 8TB (2x 4TB) | Dual-Core', 34999, 1, 18, '3 Years', 'China', 'nas', {'Bays': '2', 'Capacity': '8TB (2x 4TB WD Red)', 'Processor': 'Marvell Armada 388 Dual-Core', 'RAM': '2GB DDR3'}),
    ],
    'Rack Accessories': [
        ('APC NetShelter SX 42U Rack', 'APC', 'APC-NS42U', '42U | 600mm Wide x 1075mm Deep | Black', 44999, 1, 18, '5 Years', 'China', 'server', {'U Height': '42U', 'Width': '600mm', 'Depth': '1075mm', 'Weight Capacity': '3200 kg', 'Color': 'Black'}),
        ('APC Smart-UPS SRT 5000VA RM', 'APC', 'APC-SRT5000', '5000VA / 4500W | Online | 2U Rack-Mount', 299999, 1, 18, '3 Years', 'China', 'ups', {'Capacity': '5000VA / 4500W', 'Type': 'Double-Conversion Online', 'Form Factor': '2U Rack-Mount', 'Features': 'Network Management Card'}),
    ],
    'Industrial PLCs': [
        ('Siemens S7-1200 CPU 1214C', 'Siemens', 'SIE-S71214', '14DI/10DO/2AI | Profinet | 100KB Memory', 29999, 1, 18, '1 Year', 'Germany', 'industrial', {'Type': 'Compact PLC', 'Digital Inputs': '14', 'Digital Outputs': '10', 'Analog Inputs': '2', 'Memory': '100KB', 'Communication': 'Profinet, RS485'}),
        ('Siemens S7-1500 CPU 1515SP PC2', 'Siemens', 'SIE-S71515', 'High-Performance PLC | TIA Portal', 89999, 1, 18, '1 Year', 'Germany', 'industrial', {'Type': 'Advanced PLC', 'Memory': '1MB', 'Communication': 'Profinet, OPC UA', 'Features': 'Motion Control, Web Server'}),
        ('ABB AC500-eCo PM5033 Controller', 'ABB', 'ABB-PM5033', 'Compact PLC | 24VDC | IEC 61131-3', 34999, 1, 18, '1 Year', 'Finland', 'industrial', {'Type': 'Compact PLC', 'Memory': '512KB', 'Communication': 'Modbus, CANopen', 'I/O': 'Up to 240 modules'}),
    ],
    'Industrial Sensors': [
        ('Honeywell HumidIcon HIH6130', 'Honeywell', 'HON-HIH6130', 'Temperature & Humidity Sensor | I2C', 1999, 5, 18, '1 Year', 'China', 'industrial', {'Type': 'Temperature & Humidity', 'Range': '0-100% RH, -40 to 125C', 'Accuracy': '+/- 4% RH', 'Interface': 'I2C/SPI'}),
        ('Bosch BME280 Sensor Module', 'Bosch', 'BOS-BME280', 'Temperature/Humidity/Pressure | I2C/SPI', 999, 10, 18, '1 Year', 'China', 'industrial', {'Type': 'Environmental Sensor', 'Range': 'Temperature -40 to 85C', 'Pressure': '300-1100 hPa', 'Interface': 'I2C, SPI'}),
        ('Siemens SITRANS P DS III Pressure', 'Siemens', 'SIE-DSIII', 'Pressure Transmitter | 4-20mA | HART', 19999, 1, 18, '1 Year', 'Germany', 'industrial', {'Type': 'Pressure Transmitter', 'Output': '4-20mA, HART', 'Range': '0-400 bar', 'Accuracy': '0.025%'}),
    ],
    'Relays & Contactors': [
        ('Schneider Electric Tesys LC1D09 Contactor', 'Schneider Electric', 'SE-LC1D09', '9A Contactor | 230V Coil | 3-Pole', 2999, 1, 18, '1 Year', 'China', 'industrial', {'Type': 'Contactor', 'Current': '9A AC-3', 'Coil Voltage': '230V AC', 'Poles': '3'}),
        ('ABB AF09 Contactor', 'ABB', 'ABB-AF09', '9A Contactor | 230V Coil | Multi-Standard', 3499, 1, 18, '1 Year', 'China', 'industrial', {'Type': 'Contactor', 'Current': '9A AC-3', 'Coil Voltage': '230V AC', 'Standards': 'IEC, UL, CSA'}),
        ('Schneider Electric RXM2AB2BD Relay', 'Schneider Electric', 'SE-RXM2AB', '2-Channel Relay Module | 24VDC Coil', 1999, 1, 18, '1 Year', 'China', 'industrial', {'Type': 'Relay Module', 'Channels': '2', 'Coil Voltage': '24VDC', 'Contact Rating': '8A 250VAC'}),
    ],
    'Smart Home': [
        ('TP-Link Kasa Smart Plug EP25', 'TP-Link', 'TPL-KASAEP25', 'Smart Plug | WiFi | Energy Monitoring | 16A', 1499, 1, 18, '2 Years', 'China', 'router', {'Type': 'Smart Plug', 'Connectivity': 'WiFi', 'Max Load': '16A / 3680W', 'Features': 'Energy Monitoring, Voice Control'}),
        ('Philips Hue White Starter Kit', 'Samsung', 'PHIL-HUEWK', '2x Bulbs + Bridge | WiFi/Zigbee | Dimmable', 9999, 1, 18, '2 Years', 'China', 'speaker', {'Type': 'Smart Lighting Kit', 'Bulbs': '2x A19 E27', 'Connectivity': 'Zigbee, WiFi', 'Features': 'Dimmable, 16M Colors', 'Bridge': 'Included'}),
        ('Ring Video Doorbell 4', 'Samsung', 'RING-VDB4', '1080p | WiFi | Motion Detection | 2-Way Audio', 16999, 1, 18, '1 Year', 'China', 'cctv', {'Resolution': '1080p', 'Connectivity': 'WiFi', 'Features': 'Pre-Roll, 2-Way Audio, Motion Zones', 'Power': 'Rechargeable Battery / Hardwired'}),
    ],
    'Wearable Technology': [
        ('Samsung Galaxy Watch 6 Classic 47mm', 'Samsung', 'SAM-GW6C47', 'WearOS | BioActive Sensor | Rotating Bezel', 34999, 1, 18, '1 Year', 'Vietnam', 'smartwatch', {'Display': '1.47" Super AMOLED', 'OS': 'WearOS 4', 'Features': 'BioActive Sensor, GPS, NFC', 'Battery': '425mAh', 'Water Resistance': '5ATM + IP68'}),
        ('Samsung Galaxy Watch FE', 'Samsung', 'SAM-GWFE', 'WearOS | BioActive Sensor | 40mm', 14999, 1, 18, '1 Year', 'Vietnam', 'smartwatch', {'Display': '1.2" AMOLED', 'OS': 'WearOS 4', 'Features': 'BioActive Sensor, GPS', 'Battery': '247mAh'}),
        ('Apple Watch SE 2nd Gen', 'Apple', 'APL-AWSE2', 'watchOS | Heart Rate | Crash Detection', 29900, 1, 18, '1 Year', 'China', 'smartwatch', {'Display': '1.57" OLED', 'OS': 'watchOS 10', 'Features': 'Heart Rate, Crash Detection, GPS', 'Water Resistance': 'WR50'}),
    ],
    'Tablets': [
        ('Apple iPad 10th Gen 64GB WiFi', 'Apple', 'APL-IP1064', '10.9" Liquid Retina | A14 | 64GB | WiFi', 44900, 1, 18, '1 Year', 'China', 'tablet', {'Display': '10.9" Liquid Retina', 'Processor': 'A14 Bionic', 'Storage': '64GB', 'Camera': '12MP + 12MP Front', 'Battery': '10 hours'}),
        ('Samsung Galaxy Tab A9+ 64GB WiFi', 'Samsung', 'SAM-TABA964', '11" TFT LCD | SD 695 | 4GB | 64GB | WiFi', 22999, 1, 18, '1 Year', 'Vietnam', 'tablet', {'Display': '11" TFT LCD 90Hz', 'Processor': 'Snapdragon 695', 'RAM': '4GB', 'Storage': '64GB', 'Battery': '7040mAh'}),
        ('Samsung Galaxy Tab S9 FE 128GB', 'Samsung', 'SAM-TABFE128', '10.9" LCD | Exynos 1380 | 6GB | 128GB | S Pen', 34999, 1, 18, '1 Year', 'Vietnam', 'tablet', {'Display': '10.9" LCD 90Hz', 'Processor': 'Exynos 1380', 'RAM': '6GB', 'Storage': '128GB', 'Stylus': 'S Pen Included'}),
    ],
    'Networking Cables': [
        ('Cat6 UTP Ethernet Cable 30m', 'Zebronics', 'ZEB-CAT6-30', 'Cat6 UTP | 30m | Blue | Pure Copper', 899, 2, 18, '1 Year', 'India', 'cable', {'Type': 'Cat6 UTP', 'Length': '30m', 'Material': 'Pure Copper', 'Speed': '1 Gbps'}),
        ('Cat6 UTP Ethernet Cable 100m', 'Zebronics', 'ZEB-CAT6-100', 'Cat6 UTP | 100m | Blue | Pure Copper', 2499, 1, 18, '1 Year', 'India', 'cable', {'Type': 'Cat6 UTP', 'Length': '100m', 'Material': 'Pure Copper', 'Speed': '1 Gbps'}),
        ('Cat6a SFTP Cable 50m', 'D-Link', 'DL-CAT6A-50', 'Cat6a SFTP | 50m | Shielded | 10Gbps', 3999, 1, 18, '1 Year', 'China', 'cable', {'Type': 'Cat6a SFTP', 'Length': '50m', 'Material': 'Copper Clad Aluminum', 'Speed': '10 Gbps'}),
    ],
    'USB Hubs & Docking': [
        ('Anker 555 USB-C Hub 8-in-1', 'Samsung', 'ANK-555HUB', 'USB-C | HDMI 4K + USB-A x3 + SD + Ethernet', 4999, 1, 18, '18 Months', 'China', 'cable', {'Ports': '8-in-1', 'Video': 'HDMI 4K@30Hz', 'Data': '3x USB-A 3.0', 'Network': 'Gigabit Ethernet', 'Power': '100W PD Passthrough'}),
        ('CalDigit TS4 Thunderbolt 4 Dock', 'Samsung', 'CAL-TS4', 'Thunderbolt 4 | 18 Ports | 98W Charging', 29999, 1, 18, '2 Years', 'China', 'cable', {'Ports': '18', 'Video': 'Dual 6K or Single 8K', 'Thunderbolt': '3x TB4', 'USB': '5x USB-A + 3x USB-C', 'Power': '98W Charging'}),
        ('Lenovo ThinkPad Universal USB-C Dock', 'Lenovo', 'LEN-DOCK', 'USB-C | Dual 4K | 100W PD | 13 Ports', 12999, 1, 18, '3 Years', 'China', 'cable', {'Ports': '13', 'Video': 'Dual 4K@60Hz', 'Power': '100W PD', 'Network': 'Gigabit Ethernet'}),
    ],
    'Office Supplies - Stationery': [
        ('HP Premium A4 Copy Paper 500 sheets', 'HP', 'HP-A4PAPER', 'A4 | 80gsm | 500 Sheets | Bright White', 299, 5, 18, 'N/A', 'India', 'default', {'Size': 'A4 (210 x 297mm)', 'Weight': '80 gsm', 'Sheets': '500', 'Color': 'Bright White'}),
        ('Kangaro HD 501 Paper Shredder', 'Zebronics', 'KAN-HD501', '8-Sheet Cross Cut | P-4 | 20L Bin', 5999, 1, 18, '1 Year', 'India', 'default', {'Sheets': '8 sheets at once', 'Cut Type': 'Cross Cut P-4', 'Bin Capacity': '20L', 'Run Time': '3 minutes'}),
    ],
    'Office Furniture': [
        ('Godrej Interio Apollo Ergonomic Chair', 'Zebronics', 'GODR-APOLLO', 'High Back | Mesh | Adjustable Arms | Lumbar', 12999, 1, 18, '5 Years', 'India', 'default', {'Type': 'Executive Chair', 'Material': 'Mesh Back', 'Features': 'Adjustable Arms, Lumbar Support, Headrest', 'Weight Capacity': '120 kg'}),
        ('Featherlite Amaze Workstation', 'Zebronics', 'FEA-AMAZE', '4-Seater Workstation | Engineered Wood | 1200mm', 29999, 1, 18, '5 Years', 'India', 'default', {'Type': 'Workstation', 'Seating': '4-Person', 'Dimensions': '1200mm x 600mm x 750mm per seat', 'Material': 'Engineered Wood'}),
    ],
    # === ADDITIONAL LAPTOPS (Business, Consumer) ===
    'Consumer Laptops': [
        ('Dell Inspiron 16 5640', 'Dell', 'DELL-INS5640', '16" FHD+ | i7-1355U | 16GB | 1TB SSD', 72999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '16" FHD+', 'Processor': 'Intel Core i7-1355U', 'RAM': '16GB DDR5', 'Storage': '1TB NVMe SSD'}),
        ('HP Pavilion 15-eg3000', 'HP', 'HP-PAV15', '15.6" FHD | i5-1335U | 8GB | 512GB SSD', 52999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD IPS', 'Processor': 'Intel Core i5-1335U', 'RAM': '8GB DDR4', 'Storage': '512GB SSD'}),
        ('Lenovo IdeaPad Slim 5 14"', 'Lenovo', 'LEN-SLIM514', '14" WUXGA | i5-1335U | 8GB | 512GB SSD', 49999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '14" WUXGA', 'Processor': 'Intel Core i5-1335U', 'RAM': '8GB LPDDR5', 'Storage': '512GB SSD'}),
        ('ASUS Vivobook 14 OLED', 'ASUS', 'ASUS-VB14OLED', '14" OLED 2.8K | R7-7730U | 16GB | 512GB', 69999, 1, 18, '1 Year', 'Taiwan', 'laptop', {'Display': '14" OLED 2.8K', 'Processor': 'AMD Ryzen 7 7730U', 'RAM': '16GB LPDDR4x', 'Storage': '512GB SSD'}),
        ('HP 15s-fq5000', 'HP', 'HP-15SFQ', '15.6" FHD | i3-1215U | 8GB | 512GB SSD', 34999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Core i3-1215U', 'RAM': '8GB DDR4', 'Storage': '512GB SSD'}),
        ('Lenovo V14 G3 IAP', 'Lenovo', 'LEN-V14G3', '14" FHD | i5-1235U | 8GB | 256GB SSD', 36999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '14" FHD', 'Processor': 'Intel Core i5-1235U', 'RAM': '8GB DDR4', 'Storage': '256GB SSD'}),
        ('Dell Latitude 3440', 'Dell', 'DELL-LAT3440', '14" FHD | i5-1335U | 8GB | 256GB SSD', 45999, 1, 18, '3 Years', 'China', 'laptop', {'Display': '14" FHD', 'Processor': 'Intel Core i5-1335U', 'RAM': '8GB DDR4', 'Storage': '256GB SSD'}),
        ('ASUS Chromebook CX1500', 'ASUS', 'ASUS-CX1500', '15.6" FHD | Celeron N4500 | 4GB | 128GB eMMC', 21999, 1, 18, '1 Year', 'Taiwan', 'laptop', {'Display': '15.6" FHD', 'Processor': 'Intel Celeron N4500', 'RAM': '4GB LPDDR4x', 'Storage': '128GB eMMC', 'OS': 'ChromeOS'}),
        ('HP Chromebook 14', 'HP', 'HP-CB14', '14" HD | MediaTek MT8183 | 4GB | 64GB eMMC', 19999, 1, 18, '1 Year', 'China', 'laptop', {'Display': '14" HD', 'Processor': 'MediaTek MT8183', 'RAM': '4GB LPDDR4', 'Storage': '64GB eMMC'}),
        ('Lenovo ThinkPad L14 Gen 4', 'Lenovo', 'LEN-L14G4', '14" FHD | i5-1335U | 8GB | 256GB SSD', 51999, 1, 18, '3 Years', 'China', 'laptop', {'Display': '14" FHD IPS', 'Processor': 'Intel Core i5-1335U', 'RAM': '8GB DDR4', 'Storage': '256GB NVMe SSD', 'MIL-STD': '810H'}),
    ],
    # === WORKSTATIONS ===
    'Workstations': [
        ('Dell Precision 3680 Tower', 'Dell', 'DELL-PREC3680', 'Tower | i7-13700 | 32GB | 1TB SSD | RTX A2000', 189999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i7-13700', 'RAM': '32GB DDR5 ECC', 'GPU': 'NVIDIA RTX A2000 12GB', 'Storage': '1TB NVMe SSD'}),
        ('HP Z4 G5 Workstation', 'HP', 'HP-Z4G5', 'Tower | W5-2455X | 32GB | 1TB SSD | RTX A4000', 299999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Xeon W5-2455X', 'RAM': '32GB DDR5 ECC', 'GPU': 'NVIDIA RTX A4000 16GB', 'Storage': '1TB NVMe SSD'}),
        ('Lenovo ThinkStation P3 Tower', 'Lenovo', 'LEN-P3TWR', 'Tower | i9-13900 | 64GB | 2TB SSD | RTX A5000', 399999, 1, 18, '3 Years', 'China', 'desktop', {'Processor': 'Intel Core i9-13900', 'RAM': '64GB DDR5 ECC', 'GPU': 'NVIDIA RTX A5000 24GB', 'Storage': '2TB NVMe SSD'}),
    ],
    # === MORE MONITORS ===
    'Ultrawide Monitors': [
        ('Dell U3423WE 34" Ultrawide', 'Dell', 'DELL-U3423WE', '34" WQHD | IPS | USB-C Hub | Curved', 64999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '34 inch', 'Resolution': '3440x1440', 'Panel': 'IPS Curved', 'Refresh': '60Hz', 'Connectivity': 'USB-C 90W, HDMI, DP'}),
        ('Samsung Odyssey OLED G9 49"', 'Samsung', 'SAM-OLEDG9', '49" DQHD | OLED | 240Hz | 0.03ms', 149999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '49 inch', 'Resolution': '5120x1440', 'Panel': 'QD-OLED', 'Refresh': '240Hz', 'Response': '0.03ms GtG'}),
        ('LG 34WQ75C-B 34" Ultrawide', 'Samsung', 'LG-34WQ75C', '34" WQHD | IPS | USB-C 96K', 44999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '34 inch', 'Resolution': '3440x1440', 'Panel': 'IPS', 'Color': '98% DCI-P3', 'Connectivity': 'USB-C 96W'}),
    ],
    # === GAMING PERIPHERALS ===
    'Gaming Peripherals': [
        ('Razer Huntsman V3 Pro Analog', 'Razer', 'RAZ-HV3PA', 'Gaming Keyboard | Analog Switches | 8000Hz', 22999, 1, 18, '2 Years', 'China', 'keyboard', {'Type': 'Optical Analog', 'Switch': 'Razer Analog', 'Polling': '8000Hz', 'Backlight': 'RGB Per-Key'}),
        ('Corsair Scimitar RGB Elite Gaming Mouse', 'Corsair', 'COR-SCIMRE', 'Gaming Mouse | 18000 DPI | 12 Side Buttons', 8999, 1, 18, '2 Years', 'China', 'mouse', {'DPI': '18000', 'Buttons': '17', 'Type': 'MMO Gaming', 'Weight': '122g'}),
        ('Razer Viper Mini Signature Edition', 'Razer', 'RAZ-VMSE', 'Wireless Gaming Mouse | 30000 DPI | 49g', 19999, 1, 18, '2 Years', 'China', 'mouse', {'DPI': '30000', 'Weight': '49g', 'Connectivity': 'HyperSpeed Wireless', 'Battery': '90 hours'}),
        ('Logitech G Pro X Superlight 2', 'Logitech', 'LOG-GPXS2', 'Wireless Gaming Mouse | 32000 DPI | 60g', 14999, 1, 18, '2 Years', 'China', 'mouse', {'DPI': '32000', 'Weight': '60g', 'Connectivity': 'LIGHTSPEED', 'Battery': '95 hours'}),
        ('Corsair K70 Max RGB Gaming', 'Corsair', 'COR-K70MAX', 'Gaming Keyboard | Magnetic Switches | 8000Hz', 19999, 1, 18, '2 Years', 'China', 'keyboard', {'Type': 'Magnetic Switch', 'Polling': '8000Hz', 'Backlight': 'RGB', 'Rapid Trigger': 'Yes'}),
        ('HyperX Cloud III Wireless Gaming', 'Logitech', 'HX-CLOUD3W', 'Wireless Gaming Headset | 100hr | DTS:X', 14999, 1, 18, '2 Years', 'China', 'headphones', {'Type': 'Over-Ear Wireless', 'Battery': '120 hours', 'Audio': 'DTS:X Spatial', 'Driver': '53mm'}),
    ],
    # === NETWORKING - MORE ===
    'WiFi Mesh Systems': [
        ('TP-Link Deco XE75 3-Pack WiFi 6E', 'TP-Link', 'TPL-DECXE75-3', 'AXE5400 | Wi-Fi 6E | Tri-Band | 3-Pack', 19999, 1, 18, '3 Years', 'China', 'router', {'Speed': 'AXE5400', 'Bands': 'Tri-Band', 'Coverage': '7200 sq ft', 'Pack': '3'}),
        ('Google Nest WiFi Pro 3-Pack', 'Samsung', 'GOOG-NWP3', 'WiFi 6E | Tri-Band | 3-Pack', 24999, 1, 18, '1 Year', 'China', 'router', {'Speed': 'WiFi 6E', 'Bands': 'Tri-Band', 'Coverage': '6600 sq ft'}),
        ('ASUS ZenWiFi ET8 3-Pack', 'ASUS', 'ASUS-ZWET8', 'AXE11000 | WiFi 6E | Tri-Band | Mesh', 39999, 1, 18, '3 Years', 'Taiwan', 'router', {'Speed': 'AXE11000', 'Bands': 'Tri-Band', 'Coverage': '5500 sq ft'}),
    ],
    'PoE Switches': [
        ('TP-Link TL-SG2210MP 8-Port PoE+', 'TP-Link', 'TPL-SG2210MP', '8-Port Gigabit PoE+ | 150W Budget | Managed', 12999, 1, 18, '3 Years', 'China', 'switch', {'Ports': '8 x 1G PoE+ + 2x SFP', 'PoE Budget': '150W', 'Management': 'Smart Managed'}),
        ('Cisco CBS350-8P-2G Compact PoE', 'Cisco', 'CISCO-CBS350-8P', '8-Port PoE+ | Managed | L2', 19999, 1, 18, 'Limited Lifetime', 'China', 'switch', {'Ports': '8 x 1G PoE+ + 2x SFP', 'PoE Budget': '67W'}),
        ('Ubiquiti UniFi USW-24-PoE', 'D-Link', 'UBI-USW24P', '24-Port Gigabit PoE+ | Managed | 195W', 34999, 1, 18, '1 Year', 'China', 'switch', {'Ports': '24 x 1G PoE+', 'PoE Budget': '195W', 'Management': 'UniFi Controller'}),
    ],
    'Fiber Optic Equipment': [
        ('Cisco SFP-10G-SR 10G SFP+ Module', 'Cisco', 'CISCO-SFP10GSR', '10G SFP+ SR | 850nm | 300m Multi-Mode', 6999, 1, 18, 'Limited Lifetime', 'China', 'switch', {'Type': 'SFP+ Module', 'Speed': '10Gbps', 'Wavelength': '850nm', 'Distance': '300m'}),
        ('TP-Link TL-SM311LS SFP Module', 'TP-Link', 'TPL-SM311LS', 'SFP | 1.25G | 1310nm | 20km Single-Mode', 2499, 1, 18, '3 Years', 'China', 'switch', {'Type': 'SFP Module', 'Speed': '1.25Gbps', 'Wavelength': '1310nm', 'Distance': '20km'}),
    ],
    # === STORAGE - MORE ===
    'Enterprise Storage': [
        ('Seagate Exos X20 20TB Enterprise', 'Seagate', 'SG-EXOS20T', '20TB 7200RPM | SAS 12Gb/s | 256MB Cache', 34999, 1, 18, '5 Years', 'China', 'hdd', {'Capacity': '20TB', 'RPM': '7200', 'Interface': 'SAS 12Gb/s', 'Cache': '256MB', 'Workload': '550 TB/yr'}),
        ('WD Ultrastar DC HC580 20TB', 'Western Digital', 'WD-HC580', '20TB 7200RPM | SATA 6Gb/s | CMR', 32999, 1, 18, '5 Years', 'China', 'hdd', {'Capacity': '20TB', 'RPM': '7200', 'Interface': 'SATA III', 'Workload': '550 TB/yr'}),
        ('Samsung PM1733 3.84TB Enterprise NVMe', 'Samsung', 'SAM-PM1733', '3.84TB PCIe Gen4 | U.2 | Read Intensive', 79999, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '3.84TB', 'Interface': 'PCIe Gen4 x4', 'Sequential Read': '8000 MB/s', 'TBW': '7008 TBW'}),
    ],
    # === CCTV & SURVEILLANCE - MORE ===
    'NVR Systems': [
        ('Hikvision DS-7632NI-K2/16P NVR', 'Hikvision', 'HIK-7632NI', '32-Ch NVR | 4K | 16-Port PoE | 4 SATA', 29999, 1, 18, '3 Years', 'China', 'cctv', {'Channels': '32', 'Resolution': 'Up to 4K', 'PoE': '16 Ports', 'Storage': '4 SATA up to 10TB each'}),
        ('CP Plus 32-Ch NVR with 16-Port PoE', 'CP Plus', 'CP-32CHNVR', '32-Ch NVR | 4K | 16-Port PoE | H.265+', 24999, 1, 18, '2 Years', 'India', 'cctv', {'Channels': '32', 'Resolution': 'Up to 4K', 'PoE': '16 Ports', 'Codec': 'H.265+'}),
    ],
    'PTZ Cameras': [
        ('Hikvision DS-2DE4A425IWG-E 4MP PTZ', 'Hikvision', 'HIK-PTZ4MP', '4MP | 25x Zoom | IR 100m | Smart Tracking', 32999, 1, 18, '3 Years', 'China', 'cctv', {'Resolution': '4MP', 'Zoom': '25x Optical', 'IR Range': '100m', 'Features': 'Smart Tracking'}),
        ('CP Plus 2MP Speed Dome PTZ', 'CP Plus', 'CP-PTZ2MP', '2MP | 30x Zoom | IR 150m | Auto-Track', 18999, 1, 18, '2 Years', 'India', 'cctv', {'Resolution': '2MP', 'Zoom': '30x Optical', 'IR Range': '150m', 'Features': 'Auto-Track'}),
    ],
    # === UPS - MORE ===
    'Industrial UPS': [
        ('APC Smart-UPS SRT 10kVA Online', 'APC', 'APC-SRT10K', '10kVA / 10kW | Online | 3-Phase', 549999, 1, 18, '1 Year', 'China', 'ups', {'Capacity': '10kVA / 10kW', 'Type': 'Double-Conversion Online', 'Phase': '3-Phase', 'Features': 'Network Management Card'}),
        ('Schneider Electric Galaxy VS 10kVA', 'Schneider Electric', 'SE-GALVS', '10kVA / 10kW | Online | Modular | 3-Phase', 649999, 1, 18, '1 Year', 'China', 'ups', {'Capacity': '10kVA / 10kW', 'Type': 'Online', 'Phase': '3-Phase', 'Features': 'Hot-Swappable, Scalable'}),
    ],
    # === AUTOMATION & IoT ===
    'IoT Development Boards': [
        ('Arduino Uno R4 WiFi', 'Zebronics', 'ARD-UNOR4', 'ATmega4809 + ESP32-S3 | WiFi | 14 Digital I/O', 3999, 1, 18, '1 Year', 'China', 'industrial', {'Processor': 'Renesas RA4M1', 'WiFi': 'ESP32-S3 Module', 'Digital I/O': '14', 'Analog In': '6', 'Flash': '256KB'}),
        ('Raspberry Pi 5 8GB', 'Zebronics', 'RPI5-8GB', 'BCM2712 | Quad-A76 | 8GB RAM | WiFi 6', 8999, 1, 18, '1 Year', 'UK', 'industrial', {'Processor': 'Broadcom BCM2712', 'RAM': '8GB LPDDR4x', 'WiFi': 'WiFi 6', 'Bluetooth': '5.0', 'USB': '2x USB 3.0 + 2x USB 2.0'}),
        ('ESP32-S3 DevKitC-1', 'Zebronics', 'ESP32S3-DEV', 'Dual-Core 240MHz | WiFi + BLE | 512KB SRAM', 1299, 2, 18, '1 Year', 'China', 'industrial', {'Processor': 'Dual-Core Xtensa 240MHz', 'RAM': '512KB SRAM + 8MB PSRAM', 'WiFi': 'WiFi 802.11 b/g/n', 'Bluetooth': 'BLE 5.0', 'GPIO': '45'}),
        ('Arduino Mega 2560 Rev3', 'Zebronics', 'ARD-MEGA', 'ATmega2560 | 54 Digital I/O | 16 Analog', 4999, 1, 18, '1 Year', 'China', 'industrial', {'Processor': 'ATmega2560', 'Digital I/O': '54', 'Analog In': '16', 'Flash': '256KB', 'Clock': '16MHz'}),
    ],
    'Smart Plugs & Switches': [
        ('TP-Link Kasa Smart Wi-Fi Plug Mini', 'TP-Link', 'TPL-KASAPLUG', 'Smart Plug | WiFi | Energy Monitor | Voice Control', 999, 2, 18, '2 Years', 'China', 'router', {'Type': 'Smart Plug', 'Connectivity': 'WiFi', 'Max Load': '16A', 'Features': 'Voice Control, Energy Monitor'}),
        ('Wipro Smart LED Bulb 9W', 'Zebronics', 'WIPR-SLB9', 'Smart LED Bulb | WiFi | RGBW | 800lm', 799, 3, 18, '1 Year', 'India', 'speaker', {'Type': 'Smart LED Bulb', 'Wattage': '9W', 'Connectivity': 'WiFi', 'Colors': 'RGBW + 16M', 'Lumens': '800'}),
    ],
    # === MORE AUDIO ===
    'Soundbars': [
        ('Samsung HW-Q990D 11.1.4ch Soundbar', 'Samsung', 'SAM-HWQ990', '11.1.4ch | Dolby Atmos | Wireless Sub | Q-Symphony', 149999, 1, 18, '1 Year', 'China', 'speaker', {'Channels': '11.1.4', 'Audio': 'Dolby Atmos, DTS:X', 'Subwoofer': 'Wireless 8"', 'Features': 'Q-Symphony, SpaceFit Sound'}),
        ('JBL BAR 1300 11.1.4 Soundbar', 'JBL', 'JBL-BAR1300', '11.1.4ch | Dolby Atmos | 1170W | Wireless', 99999, 1, 18, '1 Year', 'China', 'speaker', {'Channels': '11.1.4', 'Power': '1170W', 'Audio': 'Dolby Atmos, MultiBeam', 'Subwoofer': '12" Wireless'}),
        ('Sony HT-A7000 7.1.2ch Soundbar', 'Sony', 'SONY-HTA7000', '7.1.2ch | Dolby Atmos | DTS:X | 500W', 79999, 1, 18, '1 Year', 'China', 'speaker', {'Channels': '7.1.2', 'Power': '500W', 'Audio': 'Dolby Atmos, DTS:X', 'Features': 'Vertical Surround Engine'}),
    ],
    'PA Systems': [
        ('JBL Eon One Compact Portable PA', 'JBL', 'JBL-EOC', 'Portable PA | 8" LF + 1" HF | Bluetooth | Mixer', 49999, 1, 18, '1 Year', 'China', 'speaker', {'Type': 'Portable PA', 'LF Driver': '8"', 'HF Driver': '1"', 'Power': '130W', 'Features': 'Bluetooth, 4-Channel Mixer, Reverb'}),
        ('JBL IRX108BT 8" Portable PA', 'JBL', 'JBL-IRX108', '8" Powered Speaker | Bluetooth | 1300W Peak', 34999, 1, 18, '3 Years', 'China', 'speaker', {'Type': 'Powered Speaker', 'Driver': '8"', 'Power': '1300W Peak', 'Features': 'Bluetooth, DBX AFS'}),
    ],
    # === MORE INDUSTRIAL ===
    'VFDs & Drives': [
        ('Siemens SINAMICS V20 VFD 0.75kW', 'Siemens', 'SIE-V20-075', '0.75kW VFD | 1-Phase Input | Modbus', 14999, 1, 18, '1 Year', 'Germany', 'industrial', {'Power': '0.75kW', 'Input': '1-Phase 230V', 'Communication': 'Modbus RTU', 'Protection': 'IP20'}),
        ('ABB ACS150 VFD 1.5kW', 'ABB', 'ABB-ACS150-15', '1.5kW VFD | 1-Phase | Built-in EMC Filter', 18999, 1, 18, '1 Year', 'China', 'industrial', {'Power': '1.5kW', 'Input': '1-Phase 230V', 'Features': 'Built-in EMC, PID Controller'}),
        ('Schneider Electric Altivar ATV320 VFD 2.2kW', 'Schneider Electric', 'SE-ATV320', '2.2kW VFD | 3-Phase | Modbus TCP', 24999, 1, 18, '1 Year', 'China', 'industrial', {'Power': '2.2kW', 'Input': '3-Phase 400V', 'Communication': 'Modbus TCP'}),
    ],
    'Circuit Breakers': [
        ('Schneider Electric Acti9 iC60N MCB 16A', 'Schneider Electric', 'SE-IC60N16', 'MCB 16A | C-Curve | 10kA | 1P', 599, 5, 18, '1 Year', 'China', 'industrial', {'Type': 'MCB', 'Rating': '16A', 'Curve': 'C-Curve', 'Breaking Capacity': '10kA', 'Poles': '1P'}),
        ('ABB S200 MCB 20A Circuit Breaker', 'ABB', 'ABB-S200-20', 'MCB 20A | C-Curve | 10kA | 1P', 699, 5, 18, '1 Year', 'China', 'industrial', {'Type': 'MCB', 'Rating': '20A', 'Curve': 'C-Curve', 'Breaking Capacity': '10kA'}),
        ('Siemens 5SY6 MCB 32A', 'Siemens', 'SIE-5SY6-32', 'MCB 32A | C-Curve | 10kA | 1P', 799, 5, 18, '1 Year', 'Germany', 'industrial', {'Type': 'MCB', 'Rating': '32A', 'Curve': 'C-Curve', 'Breaking Capacity': '10kA'}),
    ],
    # === CAMERA & PHOTOGRAPHY ===
    'DSLR Cameras': [
        ('Canon EOS 90D DSLR Body', 'Canon', 'CAN-E90D', '32.5MP APS-C | 10fps | 4K30 | Optical Viewfinder', 94999, 1, 18, '2 Years', 'Japan', 'camera', {'Sensor': '32.5MP APS-C CMOS', 'AF Points': '45 All Cross-Type', 'Burst': '10 fps', 'Video': '4K 30fps', 'ISO': '100-25600'}),
        ('Nikon D7500 DSLR Body', 'Canon', 'NIK-D7500', '20.9MP APS-C | 8fps | 4K30 | SnapBridge', 84999, 1, 18, '2 Years', 'Thailand', 'camera', {'Sensor': '20.9MP APS-C CMOS', 'AF Points': '51 Point', 'Burst': '8 fps', 'Video': '4K 30fps', 'ISO': '100-51200'}),
        ('Canon EOS 200D II DSLR Body', 'Canon', 'CAN-200DII', '24.1MP APS-C | 5fps | 4K | Dual Pixel AF', 54999, 1, 18, '2 Years', 'Taiwan', 'camera', {'Sensor': '24.1MP APS-C CMOS', 'AF Points': 'Dual Pixel CMOS AF', 'Burst': '5 fps', 'Video': '4K 25fps'}),
    ],
    'Mirrorless Cameras': [
        ('Sony A7 IV Full Frame Mirrorless', 'Sony', 'SONY-A7IV', '33MP Full Frame | 10fps | 4K60 | BIONZ XR', 249999, 1, 18, '2 Years', 'Thailand', 'camera', {'Sensor': '33MP Full Frame Exmor R', 'AF Points': '759 Phase-Detect', 'Burst': '10 fps', 'Video': '4K 60fps', 'ISO': '100-51200'}),
        ('Sony A6700 APS-C Mirrorless', 'Sony', 'SONY-A6700', '26MP APS-C | 11fps | 4K120 | AI AF', 139999, 1, 18, '2 Years', 'China', 'camera', {'Sensor': '26MP APS-C Exmor R', 'AF Points': '759 Phase-Detect', 'Burst': '11 fps', 'Video': '4K 120fps'}),
        ('Fujifilm X-T5 Mirrorless', 'Canon', 'FUJ-XT5', '40MP APS-C | 15fps | 6.2K30 | X-Processor 5', 159999, 1, 18, '2 Years', 'Japan', 'camera', {'Sensor': '40MP APS-C X-Trans CMOS 5 HR', 'Burst': '15 fps', 'Video': '6.2K 30fps', 'ISO': '125-12800'}),
        ('Sony ZV-E10 II Vlog Camera', 'Sony', 'SONY-ZVE10II', '26MP APS-C | 4K60 | Real-time Tracking | Built-in Mic', 74999, 1, 18, '2 Years', 'China', 'camera', {'Sensor': '26MP APS-C', 'Video': '4K 60fps', 'Features': 'Real-time Eye AF, Product Showcase'}),
    ],
    'Camera Lenses': [
        ('Sony FE 24-70mm f/2.8 GM II', 'Sony', 'SONY-FE2470GM2', 'Full Frame | f/2.8 | Linear Motors | Weather Sealed', 189999, 1, 18, '2 Years', 'Thailand', 'camera', {'Mount': 'Sony E', 'Focal Length': '24-70mm', 'Aperture': 'f/2.8', 'Weight': '695g', 'Elements': '20 elements in 15 groups'}),
        ('Canon RF 50mm f/1.8 STM', 'Canon', 'CAN-RF50F18', 'Full Frame | f/1.8 | STM | Compact', 21999, 1, 18, '1 Year', 'China', 'camera', {'Mount': 'Canon RF', 'Focal Length': '50mm', 'Aperture': 'f/1.8', 'Weight': '160g'}),
        ('Sigma 16mm f/1.4 DC DN Contemporary', 'Sony', 'SIG-16F14', 'APS-C | f/1.4 | DC DN | Compact Prime', 34999, 1, 18, '1 Year', 'Japan', 'camera', {'Mount': 'Multiple', 'Focal Length': '16mm (24mm equiv)', 'Aperture': 'f/1.4', 'Weight': '405g'}),
    ],
    'Camera Accessories': [
        ('Manfrotto Befree Advanced Tripod', 'Canon', 'MAN-BFREEADV', 'Carbon Fiber | 4-Section | 15kg Load | Ball Head', 24999, 1, 18, '2 Years', 'Italy', 'camera', {'Material': 'Carbon Fiber', 'Sections': '4', 'Max Height': '150cm', 'Folded Length': '41cm', 'Load Capacity': '15kg'}),
        ('SanDisk Extreme Pro 128GB SDXC UHS-I', 'Canon', 'SND-EP128', '128GB | 200MB/s Read | 140MB/s Write | V30', 2999, 1, 18, 'Lifetime', 'China', 'camera', {'Capacity': '128GB', 'Speed Class': 'V30 / U3 / Class 10', 'Read': '200 MB/s', 'Write': '140 MB/s'}),
    ],
    # === POWER STRIPS & SURGE ===
    'Power & Surge Protection': [
        ('Belkin 8-Outlet Surge Protector 2M', 'Samsung', 'BLK-SURGE8', '8-Outlet | 2M Cord | 2160 Joules | Surge Protection', 1999, 2, 18, '1 Year', 'China', 'ups', {'Outlets': '8', 'Cord Length': '2m', 'Joule Rating': '2160J', 'Features': 'EMI/RFI Filtering'}),
        ('APC SurgeArrest Essential 6-Out', 'APC', 'APC-SURGE6', '6-Outlet | Surge Protection | 790 Joules', 1299, 2, 18, 'Lifetime', 'China', 'ups', {'Outlets': '6', 'Joule Rating': '790J', 'Features': 'EMI Noise Filtration'}),
    ],
    # === PHONE CASES & MOBILE ===
    'Phone Cases & Protection': [
        ('Spigen Tough Armor Case iPhone 15 Pro', 'Samsung', 'SPI-TA15P', 'TPU + Polycarbonate | Kickstand | MIL-STD', 1499, 2, 18, '1 Year', 'South Korea', 'smartphone', {'Material': 'TPU + PC', 'Features': 'Kickstand, Air Cushion Tech', 'Protection': 'MIL-STD-810G'}),
        ('Spigen Ultra Hybrid Case Samsung S24 Ultra', 'Samsung', 'SPI-UH-S24U', 'Clear TPU + PC | Anti-Yellowing | Military Grade', 1299, 2, 18, '1 Year', 'South Korea', 'smartphone', {'Material': 'Clear TPU + PC', 'Features': 'Anti-Yellowing, Air Cushion'}),
        ('Tempered Glass Screen Protector Galaxy S24', 'Samsung', 'SAM-TG-S24', '9H Hardness | Oleophobic | Ultra-Clear', 399, 5, 18, 'N/A', 'China', 'smartphone', {'Material': 'Tempered Glass 9H', 'Thickness': '0.33mm', 'Features': 'Oleophobic, Anti-Fingerprint'}),
    ],
    # === POWER SUPPLIES ===
    'Power Supplies': [
        ('Corsair RM1000e 1000W 80+ Gold', 'Corsair', 'COR-RM1000E', '1000W | 80+ Gold | Fully Modular | ATX 3.0', 14999, 1, 18, '10 Years', 'China', 'psu', {'Wattage': '1000W', 'Efficiency': '80+ Gold', 'Modular': 'Fully', 'ATX': '3.0', 'Fan': '135mm'}),
        ('Corsair RM850x 850W 80+ Gold', 'Corsair', 'COR-RM850X', '850W | 80+ Gold | Fully Modular | 135mm Fan', 11999, 1, 18, '10 Years', 'China', 'psu', {'Wattage': '850W', 'Efficiency': '80+ Gold', 'Modular': 'Fully'}),
        ('EVGA SuperNOVA 750 G7 750W', 'Corsair', 'EVGA-750G7', '750W | 80+ Gold | Fully Modular | Compact', 8999, 1, 18, '10 Years', 'China', 'psu', {'Wattage': '750W', 'Efficiency': '80+ Gold', 'Modular': 'Fully', 'Length': '130mm'}),
        ('Seasonic Focus GX-1000 1000W 80+ Gold', 'Corsair', 'SEA-GX1000', '1000W | 80+ Gold | Fully Modular | 10yr', 13999, 1, 18, '10 Years', 'China', 'psu', {'Wattage': '1000W', 'Efficiency': '80+ Gold', 'Modular': 'Fully'}),
    ],
    # === CPU COOLERS ===
    'CPU Coolers': [
        ('Noctua NH-D15 chromax.black CPU Cooler', 'Corsair', 'NOC-NHD15', 'Dual Tower | 2x 140mm | 165W TDP | PWM', 8999, 1, 18, '6 Years', 'Austria', 'cooler', {'Type': 'Dual Tower', 'Fan': '2x 140mm NF-A15', 'TDP': 'Up to 165W', 'Noise': '24.6 dBA'}),
        ('Corsair iCUE H150i Elite LCD 360mm AIO', 'Corsair', 'COR-H150I', '360mm AIO Liquid | LCD Display | RGB', 24999, 1, 18, '5 Years', 'China', 'cooler', {'Type': 'AIO Liquid 360mm', 'Fan': '3x 120mm ML RGB', 'Display': '2.1" IPS LCD', 'TDP': 'Up to 300W'}),
        ('Cooler Master Hyper 212 Black Edition', 'Corsair', 'CM-H212BE', 'Tower | 120mm PWM | 4 Heat Pipes | 150W TDP', 3499, 1, 18, '2 Years', 'China', 'cooler', {'Type': 'Single Tower', 'Fan': '120mm SickleFlow', 'TDP': 'Up to 150W', 'Heat Pipes': '4'}),
    ],
    # === PC CASES ===
    'Computer Cases': [
        ('Corsair 4000D Airflow Mid-Tower', 'Corsair', 'COR-4000D', 'Mid-Tower ATX | Tempered Glass | Airflow | 2x 120mm', 7999, 1, 18, '2 Years', 'China', 'cabinet', {'Type': 'Mid-Tower ATX', 'Material': 'Steel + Tempered Glass', 'Fans': '2x 120mm', 'GPU Clearance': '360mm'}),
        ('Lian Li O11 Dynamic EVO XL', 'Corsair', 'LL-O11EXL', 'Full Tower ATX | Dual Chamber | Tempered Glass', 19999, 1, 18, '1 Year', 'China', 'cabinet', {'Type': 'Full Tower ATX', 'Material': 'Aluminum + Tempered Glass', 'Features': 'Dual Chamber, Modular'}),
        ('Fractal Design Meshify 2 Compact', 'Corsair', 'FR-MESH2C', 'Compact ATX | High Airflow Mesh | 3x 140mm', 10999, 1, 18, '2 Years', 'China', 'cabinet', {'Type': 'Compact ATX', 'Material': 'Steel + Tempered Glass', 'Fans': '3x 140mm', 'Features': 'High Airflow Mesh'}),
    ],
    # === PROJECTORS ===
    'Projectors': [
        ('Epson EB-X51 XGA Projector', 'Epson', 'EP-EBX51', '3800 Lumens | XGA | HDMI | 15000hr Lamp', 49999, 1, 18, '2 Years', 'China', 'projector', {'Brightness': '3800 Lumens', 'Resolution': 'XGA 1024x768', 'Contrast': '16000:1', 'Lamp Life': '15000 hours', 'Connectivity': 'HDMI, USB'}),
        ('Epson EB-FH52 1080p Projector', 'Epson', 'EP-EBFH52', '4000 Lumens | 1080p | HDMI | Wireless', 79999, 1, 18, '2 Years', 'China', 'projector', {'Brightness': '4000 Lumens', 'Resolution': '1080p', 'Contrast': '16000:1', 'Connectivity': 'HDMI, WiFi'}),
        ('BenQ MS560 XGA Business Projector', 'Epson', 'BENQ-MS560', '4000 Lumens | XGA | HDMI | VGA', 39999, 1, 18, '2 Years', 'China', 'projector', {'Brightness': '4000 Lumens', 'Resolution': 'XGA', 'Contrast': '20000:1', 'Lamp Life': '15000 hours'}),
    ],
    # === SCANNERS ===
    'Document Scanners': [
        ('Epson DS-530 II Document Scanner', 'Epson', 'EP-DS530II', '40ppm | Duplex | ADF 50-Sheet | USB 3.0', 34999, 1, 18, '1 Year', 'China', 'scan', {'Speed': '40 ppm', 'ADF Capacity': '50 sheets', 'Duplex': 'Auto', 'Resolution': '600 dpi', 'Interface': 'USB 3.0'}),
        ('Brother ADS-4700W Document Scanner', 'Brother', 'BRO-ADS4700W', '40ppm | Duplex | ADF 50-Sheet | WiFi', 39999, 1, 18, '1 Year', 'China', 'scan', {'Speed': '40 ppm', 'ADF Capacity': '50 sheets', 'Connectivity': 'WiFi, USB 3.0'}),
    ],
    # === SPEAKERPHONE / CONFERENCING ===
    'Video Conferencing': [
        ('Logitech Rally Bar Mini Video Bar', 'Logitech', 'LOG-RBM2', '4K | AI Auto-Frame | Mic + Speaker | USB', 189999, 1, 18, '2 Years', 'China', 'webcam', {'Camera': '4K with AI', 'Microphone': '6-mic Beamforming', 'Speaker': 'Integrated', 'Connectivity': 'USB-C, HDMI'}),
        ('Poly Studio P15 Personal Video Bar', 'Logitech', 'POLY-P15', '4K | Auto-Frame | NoiseBlockAI | USB', 59999, 1, 18, '1 Year', 'China', 'webcam', {'Camera': '4K', 'Microphone': 'Multi-Directional', 'Speaker': 'Integrated', 'Features': 'NoiseBlockAI'}),
    ],
    # === MORE BRANDS / SPECIFIC ===
    'Cable Management': [
        ('Velcro One-Wraps Cable Ties 50-Pack', 'Zebronics', 'VEL-50PACK', 'Reusable Cable Ties | 200mm | Mixed Colors', 599, 3, 18, 'N/A', 'China', 'cable', {'Type': 'Reusable Cable Ties', 'Length': '200mm', 'Quantity': '50', 'Colors': 'Mixed'}),
        ('D-Line Jumbo Cable Raceway 32mm', 'Zebronics', 'DL-JUMBO32', 'Cable Raceway | 32mm Round | 1.5m | White', 899, 2, 18, 'N/A', 'China', 'cable', {'Type': 'Cable Raceway', 'Diameter': '32mm', 'Length': '1.5m', 'Color': 'White'}),
    ],
    # === LAPTOP ACCESSORIES ===
    'Laptop Accessories': [
        ('Logitech MK270 Wireless Keyboard Mouse Combo', 'Logitech', 'LOG-MK270', 'Wireless | Full Size Keyboard | Optical Mouse | USB', 2499, 1, 18, '1 Year', 'China', 'keyboard', {'Type': 'Wireless Combo', 'Keyboard': 'Full Size', 'Mouse': 'Optical 1000 DPI', 'Battery': 'Keyboard 24mo, Mouse 12mo'}),
        ('HP USB-C Dock G5', 'HP', 'HP-USBCDOCK', 'USB-C | Dual 4K | 100W PD | 11 Ports', 14999, 1, 18, '1 Year', 'China', 'cable', {'Ports': '11', 'Video': 'Dual 4K@60Hz', 'Power': '100W PD', 'Network': 'Gigabit Ethernet'}),
        ('Lenovo ThinkPad USB-C Universal Dock', 'Lenovo', 'LEN-USBCDOCK', 'USB-C | Dual 4K | 100W PD | 10 Ports', 12999, 1, 18, '3 Years', 'China', 'cable', {'Ports': '10', 'Video': 'Dual 4K@60Hz', 'Power': '100W PD'}),
        ('Logitech Lift Vertical Ergonomic Mouse', 'Logitech', 'LOG-LIFT', 'Wireless | 4000 DPI | Vertical | Quiet Click', 5999, 1, 18, '1 Year', 'China', 'mouse', {'DPI': '4000', 'Connectivity': 'Bluetooth + Logi Bolt', 'Type': 'Vertical Ergonomic', 'Battery': '24 months'}),
        ('Logitech ERGO K860 Split Keyboard', 'Logitech', 'LOG-ERGOK860', 'Wireless | Split Design | Palm Rest | Low Profile', 11999, 1, 18, '1 Year', 'China', 'keyboard', {'Type': 'Split Ergonomic', 'Connectivity': 'Bluetooth + USB', 'Palm Rest': 'Integrated', 'Battery': '2 years'}),
        ('Belkin F4U097 USB-C to HDMI Adapter', 'Samsung', 'BLK-USBCHDMI', 'USB-C to HDMI | 4K@60Hz | Adapter', 1499, 2, 18, '2 Years', 'China', 'cable', {'Type': 'USB-C to HDMI', 'Resolution': '4K@60Hz', 'Material': 'Aluminum'}),
    ],
    # === MORE MOBILE ===
    'Mobile Accessories': [
        ('Samsung 45W Super Fast Charger Duo', 'Samsung', 'SAM-45WCHG2', '45W | Dual USB-C | Super Fast Charging', 3499, 1, 18, '1 Year', 'Vietnam', 'charger', {'Power': '45W', 'Ports': '2x USB-C', 'Features': 'Super Fast Charging 2.0'}),
        ('Anker 737 Power Bank 24000mAh 140W', 'Samsung', 'ANK-737PB', '24000mAh | 140W PD | Laptop Charging | Display', 12999, 1, 18, '18 Months', 'China', 'powerbank', {'Capacity': '24000mAh / 86.4Wh', 'Output': '140W USB-C + 24W USB-A', 'Features': 'Smart Display, Laptop Charging'}),
        ('OnePlus SUPERVOOC 100W Dual Port', 'Samsung', 'OP-SV100W', '100W | Dual Port | GaN | Foldable', 4999, 1, 18, '1 Year', 'China', 'charger', {'Power': '100W', 'Ports': 'USB-C + USB-A', 'Technology': 'GaN'}),
    ],
    # === SERVER RACKS ===
    'Server Room Equipment': [
        ('APC NetShelter SX 42U Wide Rack', 'APC', 'APC-NS42UW', '42U | 800mm Wide | 1075mm Deep | Black', 59999, 1, 18, '5 Years', 'China', 'server', {'U Height': '42U', 'Width': '800mm', 'Depth': '1075mm', 'Weight Capacity': '3200 kg'}),
        ('APC InRow RD 35kW Cooling', 'APC', 'APC-IRRD35', '35kW Row-Based Cooling | Hot Aisle Containment', 499999, 1, 18, '1 Year', 'China', 'server', {'Cooling Capacity': '35kW', 'Type': 'Row-Based', 'Features': 'Hot Aisle Containment, EC Fan'}),
    ],
    # === BATCH 3: ADDITIONAL PRODUCTS TO REACH 500+ ===
    'Laptop Accessories Bulk': [
        ('HP USB-C Travel Dock', 'HP', 'HP-USBCTD', 'USB-C | HDMI + VGA | 3x USB-A | Ethernet', 8999, 1, 18, '1 Year', 'China', 'cable', {'Ports': 'HDMI, VGA, 3x USB-A, Ethernet, USB-C', 'Power': '60W PD'}),
        ('Lenovo ThinkPad X1 Carbon Laptop Bag', 'Lenovo', 'LEN-X1BAG', '14" Laptop Bag | Messenger Style | Water Repellent', 3499, 1, 18, '1 Year', 'China', 'laptop', {'Type': 'Laptop Bag', 'Size': '14 inch', 'Material': 'Polyester', 'Features': 'Water Repellent, Padded'}),
        ('Dell Urban Backpack 15.6"', 'Dell', 'DELL-URBANBP', '15.6" Backpack | Anti-Theft | USB Charging Port', 2999, 1, 18, '1 Year', 'China', 'laptop', {'Type': 'Backpack', 'Size': '15.6 inch', 'Features': 'Anti-Theft Pocket, USB Charging'}),
        ('Targus CityGear 15.6" Laptop Case', 'Dell', 'TAR-CG156', '15.6" Briefcase | Padded | Shoulder Strap', 3999, 1, 18, '1 Year', 'China', 'laptop', {'Type': 'Briefcase', 'Size': '15.6 inch', 'Material': 'Nylon'}),
        ('HP USB-C Mini Dock', 'HP', 'HP-USBCMINI', 'USB-C | HDMI + USB-A | 100W PD | Compact', 6999, 1, 18, '1 Year', 'China', 'cable', {'Ports': 'HDMI 4K, 2x USB-A, USB-C 100W PD', 'Compact': 'Yes'}),
    ],
    'Mouse Bulk': [
        ('Logitech M185 Wireless Mouse', 'Logitech', 'LOG-M185', 'Wireless | 1000 DPI | USB Nano Receiver', 899, 2, 18, '1 Year', 'China', 'mouse', {'DPI': '1000', 'Connectivity': 'USB Nano', 'Battery': '12 months'}),
        ('Logitech M331 Silent Wireless Mouse', 'Logitech', 'LOG-M331', 'Wireless | 1000 DPI | Silent Click | USB', 1499, 2, 18, '1 Year', 'China', 'mouse', {'DPI': '1000', 'Connectivity': 'USB Nano', 'Battery': '24 months', 'Silent': 'Yes'}),
        ('HP USB Wired Mouse 1000', 'HP', 'HP-MS1000', 'Wired | 1600 DPI | Optical | USB', 499, 3, 18, '1 Year', 'China', 'mouse', {'DPI': '1600', 'Connectivity': 'USB Wired', 'Buttons': '3'}),
        ('Dell MS116 USB Wired Mouse', 'Dell', 'DELL-MS116', 'Wired | 1000 DPI | Optical | USB', 499, 3, 18, '1 Year', 'China', 'mouse', {'DPI': '1000', 'Connectivity': 'USB Wired', 'Buttons': '3'}),
        ('Zebronics Zeb-Optima Wireless Mouse', 'Zebronics', 'ZEB-OPTIMA', 'Wireless | 1200 DPI | USB | Ergonomic', 499, 3, 18, '1 Year', 'India', 'mouse', {'DPI': '1200', 'Connectivity': 'USB Nano', 'Battery': '12 months'}),
    ],
    'Keyboard Bulk': [
        ('Logitech K120 USB Keyboard', 'Logitech', 'LOG-K120', 'Wired | USB | Full Size | Spill Resistant', 699, 3, 18, '1 Year', 'China', 'keyboard', {'Type': 'Membrane', 'Connectivity': 'USB', 'Keys': '104', 'Features': 'Spill Resistant'}),
        ('HP USB Keyboard K1500', 'HP', 'HP-K1500', 'Wired | USB | Full Size | Curved Keys', 799, 3, 18, '1 Year', 'China', 'keyboard', {'Type': 'Membrane', 'Connectivity': 'USB', 'Keys': '104', 'Features': 'Curved Keys, Spill Resistant'}),
        ('Dell KB216 Wired Keyboard', 'Dell', 'DELL-KB216', 'Wired | USB | Full Size | Multimedia Keys', 899, 3, 18, '1 Year', 'China', 'keyboard', {'Type': 'Membrane', 'Connectivity': 'USB', 'Keys': '104', 'Features': 'Multimedia Keys'}),
        ('Zebronics Zeb-Transformer Keyboard Mouse Combo', 'Zebronics', 'ZEB-COMBO1', 'Wired Combo | Keyboard + Mouse | RGB | Gaming', 1299, 2, 18, '1 Year', 'India', 'keyboard', {'Type': 'Membrane Combo', 'Connectivity': 'USB', 'Features': 'RGB Backlit, Gaming'}),
        ('Lenovo Preferred Pro USB Keyboard', 'Lenovo', 'LEN-PPK', 'Wired | USB | Full Size | Spill Resistant', 999, 3, 18, '1 Year', 'China', 'keyboard', {'Type': 'Membrane', 'Connectivity': 'USB', 'Keys': '104'}),
    ],
    'Monitor Bulk': [
        ('Dell E2422H 24" FHD', 'Dell', 'DELL-E2422H', '24" FHD | IPS | VGA + DP | Height Adjust', 13999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '24 inch', 'Resolution': '1920x1080', 'Panel': 'IPS', 'Connectivity': 'VGA, DP'}),
        ('HP V24i FHD Monitor', 'HP', 'HP-V24I', '24" FHD | IPS | HDMI + VGA', 11999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '24 inch', 'Resolution': '1920x1080', 'Panel': 'IPS', 'Connectivity': 'HDMI, VGA'}),
        ('Lenovo ThinkVision E24-40 24" FHD', 'Lenovo', 'LEN-E2440', '24" FHD | IPS | HDMI + VGA + USB-C | TUV Eye Comfort', 13999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '24 inch', 'Resolution': '1920x1080', 'Panel': 'IPS', 'TUV': 'Low Blue Light'}),
        ('Dell P2425H 24" FHD', 'Dell', 'DELL-P2425H', '24" FHD | IPS | HDMI + DP + VGA | Height Adjust', 14999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '24 inch', 'Resolution': '1920x1080', 'Panel': 'IPS', 'Ergonomics': 'Height/Tilt/Swivel/Pivot'}),
        ('Samsung F27T700QQC 27" FHD IPS', 'Samsung', 'SAM-FT700', '27" FHD | IPS | 75Hz | AMD FreeSync | Borderless', 16999, 1, 18, '3 Years', 'China', 'monitor', {'Size': '27 inch', 'Resolution': '1920x1080', 'Panel': 'IPS', 'Refresh': '75Hz', 'Features': 'FreeSync, Borderless'}),
    ],
    'SSD Bulk': [
        ('Kingston A400 240GB SATA', 'Kingston', 'KNG-A400-240', '240GB SATA III | 500/320 MB/s', 2199, 2, 18, '3 Years', 'China', 'ssd', {'Capacity': '240GB', 'Interface': 'SATA III', 'Read': '500 MB/s', 'Write': '320 MB/s'}),
        ('Kingston A400 480GB SATA', 'Kingston', 'KNG-A400-480', '480GB SATA III | 500/450 MB/s', 3299, 1, 18, '3 Years', 'China', 'ssd', {'Capacity': '480GB', 'Interface': 'SATA III', 'Read': '500 MB/s', 'Write': '450 MB/s'}),
        ('Samsung 870 EVO 250GB SATA', 'Samsung', 'SAM-870E250', '250GB SATA III | 560/530 MB/s', 3499, 2, 18, '5 Years', 'China', 'ssd', {'Capacity': '250GB', 'Interface': 'SATA III', 'Read': '560 MB/s', 'Write': '530 MB/s'}),
        ('WD Blue SN580 500GB NVMe', 'Western Digital', 'WD-SN580-500', '500GB PCIe Gen4 | 4000/3600 MB/s', 3999, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '500GB', 'Interface': 'PCIe Gen4', 'Read': '4000 MB/s', 'Write': '3600 MB/s'}),
        ('Crucial P3 Plus 500GB NVMe', 'Kingston', 'CRU-P3P500', '500GB PCIe Gen4 | 5000/4200 MB/s', 3699, 1, 18, '5 Years', 'China', 'ssd', {'Capacity': '500GB', 'Interface': 'PCIe Gen4', 'Read': '5000 MB/s', 'Write': '4200 MB/s'}),
        ('Samsung T7 Shield 1TB Portable', 'Samsung', 'SAM-T7SHIELD', '1TB Portable | USB 3.2 | IP65 | 1050/1000 MB/s', 10999, 1, 18, '3 Years', 'China', 'ssd', {'Capacity': '1TB', 'Interface': 'USB 3.2 Gen2', 'Read': '1050 MB/s', 'Protection': 'IP65'}),
    ],
    'RAM Bulk': [
        ('Kingston ValueRAM 8GB DDR4', 'Kingston', 'KNG-VR8D4', '8GB DDR4-2666MHz | CL19', 1999, 2, 18, 'Lifetime', 'China', 'ram', {'Capacity': '8GB', 'Type': 'DDR4', 'Speed': '2666 MHz', 'CAS': 'CL19'}),
        ('Kingston ValueRAM 16GB DDR4', 'Kingston', 'KNG-VR16D4', '16GB DDR4-3200MHz | CL22', 3499, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '16GB', 'Type': 'DDR4', 'Speed': '3200 MHz', 'CAS': 'CL22'}),
        ('Corsair Vengeance 16GB DDR5-6000', 'Corsair', 'COR-VEN16D5-6K', '16GB DDR5-6000MHz | CL36', 6999, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '16GB', 'Type': 'DDR5', 'Speed': '6000 MHz', 'CAS': 'CL36'}),
        ('Kingston Fury Beast 64GB DDR5', 'Kingston', 'KNG-FB64D5', '64GB DDR5-5200MHz | CL40 | Kit of 2', 19999, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '64GB (2x32)', 'Type': 'DDR5', 'Speed': '5200 MHz', 'CAS': 'CL40'}),
        ('G.Skill Trident Z5 32GB DDR5-6400', 'Corsair', 'GS-TZ532', '32GB DDR5-6400MHz | CL32 | RGB', 14999, 1, 18, 'Lifetime', 'China', 'ram', {'Capacity': '32GB (2x16)', 'Type': 'DDR5', 'Speed': '6400 MHz', 'CAS': 'CL32', 'RGB': 'Yes'}),
    ],
    'HDD Bulk': [
        ('Seagate Barracuda 1TB', 'Seagate', 'SG-BAR-1T', '1TB 7200RPM SATA III | 64MB Cache', 2999, 2, 18, '2 Years', 'China', 'hdd', {'Capacity': '1TB', 'RPM': '7200', 'Interface': 'SATA III', 'Cache': '64MB'}),
        ('WD Red Plus 2TB NAS', 'Western Digital', 'WD-RP2T', '2TB NAS 5400RPM | 256MB Cache | CMR', 5999, 1, 18, '3 Years', 'China', 'hdd', {'Capacity': '2TB', 'RPM': '5400', 'Interface': 'SATA III', 'Workload': '180 TB/yr'}),
        ('Seagate IronWolf 2TB NAS', 'Seagate', 'SG-IW2T', '2TB NAS 7200RPM | 256MB Cache | CMR', 6499, 1, 18, '3 Years', 'China', 'hdd', {'Capacity': '2TB', 'RPM': '7200', 'Cache': '256MB'}),
        ('WD Red Plus 8TB NAS', 'Western Digital', 'WD-RP8T', '8TB NAS 5640RPM | 256MB Cache', 19999, 1, 18, '3 Years', 'China', 'hdd', {'Capacity': '8TB', 'RPM': '5640', 'Cache': '256MB', 'Workload': '180 TB/yr'}),
    ],
    'Networking Bulk': [
        ('TP-Link TL-SG1005D 5-Port Switch', 'TP-Link', 'TPL-SG1005D', '5-Port Gigabit | Plug-and-Play', 1499, 2, 18, 'Lifetime', 'China', 'switch', {'Ports': '5 x Gigabit', 'Switching Capacity': '10 Gbps'}),
        ('TP-Link TL-SG1008D 8-Port Switch', 'TP-Link', 'TPL-SG1008D', '8-Port Gigabit | Plug-and-Play | Metal', 2499, 2, 18, 'Lifetime', 'China', 'switch', {'Ports': '8 x Gigabit', 'Switching Capacity': '16 Gbps'}),
        ('D-Link DGS-1005D 5-Port Switch', 'D-Link', 'DL-DGS1005D', '5-Port Gigabit | Desktop | Green Ethernet', 1499, 2, 18, 'Lifetime', 'Taiwan', 'switch', {'Ports': '5 x Gigabit', 'Features': 'Green Ethernet'}),
        ('TP-Link Archer C6 AC1200 Router', 'TP-Link', 'TPL-ARCHC6', 'AC1200 | Dual Band | MU-MIMO | 4 Gigabit LAN', 3299, 1, 18, '3 Years', 'China', 'router', {'Speed': 'AC1200', 'Bands': 'Dual Band', 'Ports': '4x Gigabit LAN + 1x WAN', 'Features': 'MU-MIMO, IPv6'}),
        ('TP-Link Archer AX10 AX1500 Router', 'TP-Link', 'TPL-AX10', 'AX1500 | Wi-Fi 6 | Gigabit | 4 Antenna', 3999, 1, 18, '3 Years', 'China', 'router', {'Speed': 'AX1500', 'Bands': 'Dual Band', 'Antenna': '4x Fixed'}),
    ],
    'Printer Supplies': [
        ('HP 305A Black Toner CE410A', 'HP', 'HP-305A-BK', 'Black Toner | 2800 Pages | LaserJet', 7999, 1, 18, 'N/A', 'China', 'printer', {'Color': 'Black', 'Yield': '2800 pages', 'Compatible': 'M451, M475'}),
        ('HP 305A Cyan Toner CE411A', 'HP', 'HP-305A-CY', 'Cyan Toner | 3000 Pages | LaserJet', 9499, 1, 18, 'N/A', 'China', 'printer', {'Color': 'Cyan', 'Yield': '3000 pages', 'Compatible': 'M451, M475'}),
        ('HP 305A Yellow Toner CE412A', 'HP', 'HP-305A-YL', 'Yellow Toner | 3000 Pages | LaserJet', 9499, 1, 18, 'N/A', 'China', 'printer', {'Color': 'Yellow', 'Yield': '3000 pages'}),
        ('HP 305A Magenta Toner CE413A', 'HP', 'HP-305A-MG', 'Magenta Toner | 3000 Pages | LaserJet', 9499, 1, 18, 'N/A', 'China', 'printer', {'Color': 'Magenta', 'Yield': '3000 pages'}),
        ('Brother TN-2365 High Yield Toner', 'Brother', 'BRO-TN2365', 'Black Toner | 3000 Pages | HL-L2350DW', 5499, 1, 18, 'N/A', 'China', 'printer', {'Color': 'Black', 'Yield': '3000 pages'}),
        ('Epson 664 Black Ink Bottle', 'Epson', 'EP-664BK', 'Black Ink | 4500 Pages | EcoTank', 599, 3, 18, 'N/A', 'Indonesia', 'printer', {'Color': 'Black', 'Yield': '4500 pages', 'Compatible': 'L3110, L3150'}),
        ('Epson 664 Cyan Ink Bottle', 'Epson', 'EP-664CY', 'Cyan Ink | 7500 Pages | EcoTank', 599, 3, 18, 'N/A', 'Indonesia', 'printer', {'Color': 'Cyan', 'Yield': '7500 pages'}),
        ('Epson 664 Magenta Ink Bottle', 'Epson', 'EP-664MG', 'Magenta Ink | 7500 Pages | EcoTank', 599, 3, 18, 'N/A', 'Indonesia', 'printer', {'Color': 'Magenta', 'Yield': '7500 pages'}),
        ('Epson 664 Yellow Ink Bottle', 'Epson', 'EP-664YL', 'Yellow Ink | 7500 Pages | EcoTank', 599, 3, 18, 'N/A', 'Indonesia', 'printer', {'Color': 'Yellow', 'Yield': '7500 pages'}),
    ],
    'Network Cables Bulk': [
        ('Cat5e UTP Cable 30m', 'Zebronics', 'ZEB-CAT5E30', 'Cat5e UTP | 30m | Blue | Pure Copper', 699, 2, 18, '1 Year', 'India', 'cable', {'Type': 'Cat5e UTP', 'Length': '30m', 'Speed': '100 Mbps'}),
        ('Cat6 Patch Cable 3m', 'Zebronics', 'ZEB-CAT6P3', 'Cat6 STP | 3m | Gray | RJ45', 299, 5, 18, '1 Year', 'India', 'cable', {'Type': 'Cat6 STP', 'Length': '3m', 'Speed': '1 Gbps'}),
        ('Cat6 Patch Cable 5m', 'Zebronics', 'ZEB-CAT6P5', 'Cat6 STP | 5m | Gray | RJ45', 399, 5, 18, '1 Year', 'India', 'cable', {'Type': 'Cat6 STP', 'Length': '5m', 'Speed': '1 Gbps'}),
        ('Fiber Patch Cord LC-LC 3m SM', 'D-Link', 'DL-FPLC3', 'LC-LC | Single-Mode | 3m | OS2', 1499, 2, 18, '1 Year', 'China', 'cable', {'Type': 'LC-LC SM', 'Length': '3m', 'Mode': 'OS2 Single-Mode'}),
    ],
    'Mobile Accessories Bulk': [
        ('Samsung 25W USB-C Fast Charger 2-Pack', 'Samsung', 'SAM-25W2PK', '25W USB-C | 2-Pack | Super Fast Charging', 2999, 1, 18, '1 Year', 'Vietnam', 'charger', {'Power': '25W', 'Quantity': '2', 'Port': 'USB-C'}),
        ('Anker PowerDrive III 2-Port Car Charger', 'Samsung', 'ANK-CARCHG', '2-Port Car Charger | 48W | USB-C + USB-A', 1999, 2, 18, '18 Months', 'China', 'charger', {'Power': '48W', 'Ports': 'USB-C + USB-A', 'Features': 'Car Charger'}),
        ('Belkin 3-in-1 Wireless Charging Pad', 'Samsung', 'BLK-3IN1', '3-in-1 | Qi | iPhone + AirPods + Apple Watch', 5999, 1, 18, '2 Years', 'China', 'charger', {'Type': '3-in-1 Wireless', 'Compatible': 'iPhone, AirPods, Apple Watch', 'Power': '7.5W Qi'}),
        ('Spigen Tough Armor Case iPhone 15', 'Samsung', 'SPI-TA15', 'TPU + PC | Kickstand | Air Cushion', 1299, 2, 18, '1 Year', 'South Korea', 'smartphone', {'Material': 'TPU + PC', 'Features': 'Kickstand, Air Cushion Tech'}),
        ('Belkin 20000mAh Power Bank PD 20W', 'Samsung', 'BLK-PB20K', '20000mAh | 20W PD | Dual USB + USB-C', 3499, 1, 18, '2 Years', 'China', 'powerbank', {'Capacity': '20000mAh', 'Output': '20W USB-C + 2x USB-A'}),
    ],
    'Office Supplies Bulk': [
        ('HP Copy Plus A3 Paper 500 Sheets', 'HP', 'HP-A3PAPER', 'A3 | 80gsm | 500 Sheets', 599, 3, 18, 'N/A', 'India', 'default', {'Size': 'A3', 'Weight': '80 gsm', 'Sheets': '500'}),
        ('Kangaro DH 210 Heavy Duty Hole Punch', 'Zebronics', 'KAN-DH210', '30-Sheet Capacity | Heavy Duty | Chrome', 2499, 1, 18, '1 Year', 'India', 'default', {'Capacity': '30 sheets', 'Type': 'Heavy Duty', 'Material': 'Chrome Plated'}),
        ('Deli E510 Electric Pencil Sharpener', 'Zebronics', 'DEL-E510', 'Electric Sharpener | Auto-Stop | Helical Blade', 1499, 1, 18, '1 Year', 'China', 'default', {'Type': 'Electric', 'Features': 'Auto-Stop, Helical Blade', 'Pencil Diameter': '6-8mm'}),
        ('Rorito Maxtron Pens 10 Pack', 'Zebronics', 'ROR-MAX10', 'Gel Pen | 0.5mm | Blue | Pack of 10', 149, 5, 18, 'N/A', 'India', 'default', {'Type': 'Gel Pen', 'Tip': '0.5mm', 'Color': 'Blue', 'Quantity': '10'}),
        ('Classmate Pulse Notebook A4 200 Pages', 'Zebronics', 'CLP-A4200', 'A4 | 200 Pages | 80gsm | Ruled', 149, 5, 18, 'N/A', 'India', 'default', {'Size': 'A4', 'Pages': '200', 'Weight': '80 gsm', 'Type': 'Ruled'}),
    ],
    'Industrial Sensors Bulk': [
        ('Siemens SITRANS LU240 Ultrasonic', 'Siemens', 'SIE-LU240', 'Ultrasonic Level Transmitter | 0-20m', 49999, 1, 18, '1 Year', 'Germany', 'industrial', {'Type': 'Ultrasonic Level', 'Range': '0-20m', 'Output': '4-20mA HART'}),
        ('ABB 266DS Differential Pressure', 'ABB', 'ABB-266DS', 'Differential Pressure | 0-10 bar | 4-20mA HART', 39999, 1, 18, '1 Year', 'Italy', 'industrial', {'Type': 'Differential Pressure', 'Range': '0-10 bar', 'Output': '4-20mA HART'}),
        ('Honeywell SmartLine STG700 Pressure', 'Honeywell', 'HON-STG700', 'Gauge Pressure | 0-100 bar | HART', 44999, 1, 18, '1 Year', 'USA', 'industrial', {'Type': 'Gauge Pressure', 'Range': '0-100 bar', 'Output': '4-20mA HART'}),
        ('Schneider Electric MagneFlow 280 Flowmeter', 'Schneider Electric', 'SE-MF280', 'Electromagnetic Flowmeter | DN80', 89999, 1, 18, '1 Year', 'China', 'industrial', {'Type': 'Electromagnetic', 'Size': 'DN80', 'Output': '4-20mA + Pulse'}),
    ],
    'Industrial Relays Bulk': [
        ('Omron G2R-1-SND 24VDC Relay', 'ABB', 'OMR-G2R1', '16A Relay | 24VDC Coil | SPDT', 899, 5, 18, '5 Years', 'China', 'industrial', {'Type': 'General Purpose Relay', 'Current': '16A', 'Coil': '24VDC', 'Contacts': 'SPDT'}),
        ('Finder 40.61.9.024.0000 Relay', 'ABB', 'FND-4061', '16A Relay | 24VDC | SPDT | LED Indicator', 999, 5, 18, '5 Years', 'China', 'industrial', {'Type': 'General Purpose Relay', 'Current': '16A', 'Coil': '24VDC', 'Features': 'LED Indicator'}),
        ('Schneider Electric RXM4AB2BD 4-Channel Relay', 'Schneider Electric', 'SE-RXM4', '4-Channel Relay Module | 24VDC | DIN Rail Mount', 3499, 1, 18, '1 Year', 'China', 'industrial', {'Type': 'Relay Module', 'Channels': '4', 'Coil': '24VDC'}),
    ],
    'Smart Home Bulk': [
        ('TP-Link Tapo P110 Smart Plug', 'TP-Link', 'TPL-TAPOP110', 'Smart Plug | WiFi | Energy Monitor | Voice Control', 1799, 2, 18, '2 Years', 'China', 'router', {'Type': 'Smart Plug', 'Connectivity': 'WiFi', 'Features': 'Energy Monitor, Voice Control'}),
        ('Philips Hue Go Portable Lamp', 'Samsung', 'PHIL-HUEGO', 'Portable Smart Lamp | 16M Colors | WiFi/Zigbee', 12999, 1, 18, '2 Years', 'China', 'speaker', {'Type': 'Portable Lamp', 'Colors': '16M', 'Battery': '2 hours', 'Connectivity': 'Zigbee + Bluetooth'}),
        ('Google Nest Hub Max 10"', 'Samsung', 'GOOG-NHMAX', '10" Smart Display | Speaker | Camera | Assistant', 19999, 1, 18, '1 Year', 'China', 'speaker', {'Display': '10" HD', 'Camera': '6.5MP Nest Cam', 'Speaker': 'Stereo', 'Features': 'Google Assistant'}),
        ('Amazon Echo Dot 5th Gen', 'Samsung', 'AMZ-EDOT5', 'Smart Speaker | Alexa | LED Clock | Bluetooth', 4999, 1, 18, '1 Year', 'China', 'speaker', {'Type': 'Smart Speaker', 'Features': 'Alexa, LED Clock', 'Connectivity': 'WiFi + Bluetooth'}),
    ],
    'Wearables Bulk': [
        ('Noise ColorFit Pro 5', 'Samsung', 'NOI-CFP5', '1.85" AMOLED | SpO2 | Heart Rate | 100+ Sports', 4999, 1, 18, '1 Year', 'China', 'smartwatch', {'Display': '1.85" AMOLED', 'Features': 'SpO2, Heart Rate, GPS', 'Sports': '100+', 'Battery': '7 days'}),
        ('Fire-Boltt Phoenix Ultra', 'Samsung', 'FB-PULTRA', '1.39" AMOLED | Bluetooth Calling | AI Voice', 3999, 1, 18, '1 Year', 'China', 'smartwatch', {'Display': '1.39" AMOLED', 'Features': 'Bluetooth Calling, AI Voice', 'Battery': '7 days'}),
        ('Amazfit Bip 5', 'Samsung', 'AMZ-BIP5', '1.91" GPS | SpO2 | Heart Rate | 7-Day Battery', 8999, 1, 18, '1 Year', 'China', 'smartwatch', {'Display': '1.91" LCD', 'Features': 'GPS, SpO2, Heart Rate', 'Battery': '14 days'}),
    ],
    'Gaming Console Accessories': [
        ('Logitech G923 Racing Wheel', 'Logitech', 'LOG-G923', 'Racing Wheel | TRUEFORCE | PS5/PS4/PC', 34999, 1, 18, '2 Years', 'China', 'mouse', {'Type': 'Racing Wheel', 'Force Feedback': 'TRUEFORCE', 'Compatible': 'PS5/PS4/PC', 'Pedals': 'Included'}),
        ('Razer Kishi V2 Mobile Controller', 'Razer', 'RAZ-KISHI2', 'Mobile Controller | USB-C | Android/iPhone', 8999, 1, 18, '1 Year', 'China', 'mouse', {'Type': 'Mobile Controller', 'Connectivity': 'USB-C', 'Compatible': 'Android & iPhone'}),
        ('Corsair HS65 Surround Gaming Headset', 'Corsair', 'COR-HS65', 'Gaming Headset | 7.1 Surround | Flip-to-Mute | 50mm', 5999, 1, 18, '2 Years', 'China', 'headphones', {'Type': 'Wired Gaming', 'Driver': '50mm', 'Surround': '7.1', 'Mic': 'Flip-to-Mute'}),
    ],
}
