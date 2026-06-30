import os
import sys
from django.core.management.base import BaseCommand
from apps.categories.models import Category


class Command(BaseCommand):
    help = 'Seed complete B2B electronics category hierarchy (100+ categories)'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear all categories first')

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing all categories...')
            Category.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared.'))

        self.stdout.write(self.style.WARNING('\nSeeding B2B Electronics Categories...\n'))

        CATEGORY_TREE = {
            'Electronics': {
                'is_featured': True,
                'children': {
                    'Cameras & Photography': {
                        'children': {
                            'DSLR Cameras': {},
                            'Mirrorless Cameras': {},
                            'Action Cameras': {},
                            'Instant Cameras': {},
                            'Camera Lenses': {},
                            'Camera Tripods': {},
                            'Camera Bags & Cases': {},
                            'Flash & Lighting': {},
                            'Memory Cards': {},
                            'Camera Batteries': {},
                        },
                    },
                    'CCTV & Surveillance': {
                        'children': {
                            'IP Cameras': {},
                            'Analog Cameras': {},
                            'PTZ Cameras': {},
                            'NVR Recorders': {},
                            'DVR Recorders': {},
                            'CCTV Kits': {},
                            'Video Door Phones': {},
                            'Access Control': {},
                            'Biometric Devices': {},
                            'CCTV Cables': {},
                        },
                    },
                    'Computer Peripherals': {
                        'children': {
                            'Mice': {},
                            'Keyboards': {},
                            'Mechanical Keyboards': {},
                            'Gaming Keyboards': {},
                            'Wireless Keyboards': {},
                            'Webcams': {},
                            'Headsets': {},
                            'Graphics Tablets': {},
                            'Stylus Pens': {},
                            'KVM Switches': {},
                        },
                    },
                    'Desktops & Monitors': {
                        'children': {
                            'Desktop PCs': {},
                            'All-in-One PCs': {},
                            'Mini PCs': {},
                            'LCD Monitors': {},
                            'LED Monitors': {},
                            'Curved Monitors': {},
                            'Gaming Monitors': {},
                            'Ultrawide Monitors': {},
                            'Portable Monitors': {},
                            'Monitor Arms': {},
                        },
                    },
                    'Laptops': {
                        'children': {
                            'Business Laptops': {},
                            'Gaming Laptops': {},
                            'Ultrabooks': {},
                            'Workstation Laptops': {},
                            '2-in-1 Laptops': {},
                            'Chromebooks': {},
                            'Laptop Bags': {},
                            'Laptop Stands': {},
                            'Laptop Cooling Pads': {},
                            'Laptop Batteries': {},
                        },
                    },
                    'Printers & Scanners': {
                        'children': {
                            'Laser Printers': {},
                            'Inkjet Printers': {},
                            'Dot Matrix Printers': {},
                            'Label Printers': {},
                            'Receipt Printers': {},
                            '3D Printers': {},
                            'Barcode Scanners': {},
                            'Document Scanners': {},
                            'POS Machines': {},
                            'Printer Cartridges': {},
                            'Printer Toners': {},
                        },
                    },
                    'Networking': {
                        'is_featured': True,
                        'children': {
                            'Wireless Routers': {},
                            'Mesh WiFi Systems': {},
                            'Modem Routers': {},
                            'Network Switches': {},
                            'Managed Switches': {},
                            'Unmanaged Switches': {},
                            'PoE Switches': {},
                            'Firewalls': {},
                            'Access Points': {},
                            'WiFi Extenders': {},
                            'Network Cables': {},
                            'Patch Panels': {},
                            'Structured Cabling': {},
                        },
                    },
                    'Storage & Memory': {
                        'children': {
                            'SSD Drives': {},
                            'NVMe SSD': {},
                            'SATA SSD': {},
                            'Portable SSD': {},
                            'HDD Drives': {},
                            'External Hard Drives': {},
                            'NAS Devices': {},
                            'RAID Arrays': {},
                            'RAM Modules': {},
                            'DDR4 RAM': {},
                            'DDR5 RAM': {},
                            'USB Flash Drives': {},
                            'Memory Cards': {},
                            'Card Readers': {},
                        },
                    },
                    'Computer Components': {
                        'is_featured': True,
                        'children': {
                            'Processors': {},
                            'Intel Processors': {},
                            'AMD Processors': {},
                            'Motherboards': {},
                            'Intel Motherboards': {},
                            'AMD Motherboards': {},
                            'Graphics Cards': {},
                            'NVIDIA GPUs': {},
                            'AMD GPUs': {},
                            'Power Supplies': {},
                            'Computer Cabinets': {},
                            'CPU Coolers': {},
                            'Case Fans': {},
                            'Thermal Paste': {},
                            'Front Panels': {},
                        },
                    },
                    'Audio & Video': {
                        'children': {
                            'Speakers': {},
                            'Bookshelf Speakers': {},
                            'Tower Speakers': {},
                            'Soundbars': {},
                            'Subwoofers': {},
                            'Headphones': {},
                            'Over-Ear Headphones': {},
                            'In-Ear Headphones': {},
                            'Earbuds': {},
                            'TWS Earbuds': {},
                            'Microphones': {},
                            'Condenser Microphones': {},
                            'Wireless Microphones': {},
                            'Amplifiers': {},
                            'AV Receivers': {},
                            'Projectors': {},
                            'Home Theater Systems': {},
                        },
                    },
                    'Power & UPS': {
                        'is_featured': True,
                        'children': {
                            'Online UPS': {},
                            'Offline UPS': {},
                            'Line-Interactive UPS': {},
                            'Home UPS': {},
                            'Industrial UPS': {},
                            'Inverters': {},
                            'Inverter Batteries': {},
                            'Solar Inverters': {},
                            'Voltage Stabilizers': {},
                            'Power Strips': {},
                            'Surge Protectors': {},
                            'PDUs': {},
                        },
                    },
                    'Industrial Electronics': {
                        'children': {
                            'PLCs': {},
                            'HMIs': {},
                            'VFDs': {},
                            'Sensors': {},
                            'Temperature Sensors': {},
                            'Proximity Sensors': {},
                            'Pressure Sensors': {},
                            'Relays': {},
                            'Contactors': {},
                            'Drives': {},
                            'Transformers': {},
                            'Circuit Breakers': {},
                            'Industrial Cables': {},
                        },
                    },
                    'Automation & IoT': {
                        'children': {
                            'Smart Home Hubs': {},
                            'Smart Plugs': {},
                            'Smart Lights': {},
                            'Smart Locks': {},
                            'Smart Cameras': {},
                            'Smart Sensors': {},
                            'Smart Thermostats': {},
                            'Smart Speakers': {},
                            'IoT Modules': {},
                            'Arduino Boards': {},
                            'Raspberry Pi': {},
                            'Development Boards': {},
                        },
                    },
                    'Mobile & Accessories': {
                        'children': {
                            'Smartphones': {},
                            'Feature Phones': {},
                            'Phone Cases': {},
                            'Screen Protectors': {},
                            'Power Banks': {},
                            'Car Chargers': {},
                            'Wall Chargers': {},
                            'Fast Chargers': {},
                            'USB Cables': {},
                            'Type-C Cables': {},
                            'Lightning Cables': {},
                            'Wireless Chargers': {},
                            'Phone Holders': {},
                            'Selfie Sticks': {},
                        },
                    },
                    'Wearable Technology': {
                        'children': {
                            'Smart Watches': {},
                            'Fitness Bands': {},
                            'Smart Glasses': {},
                            'VR Headsets': {},
                            'Sport Cameras': {},
                        },
                    },
                    'Tablets & E-Readers': {
                        'children': {
                            'Android Tablets': {},
                            'iPad': {},
                            'Windows Tablets': {},
                            'Drawing Tablets': {},
                            'E-Readers': {},
                            'Tablet Accessories': {},
                            'Tablet Stands': {},
                            'Stylus Pens': {},
                        },
                    },
                    'Server & Enterprise': {
                        'children': {
                            'Rack Servers': {},
                            'Tower Servers': {},
                            'Blade Servers': {},
                            'Server Racks': {},
                            'Server UPS': {},
                            'Enterprise SSD': {},
                            'Enterprise HDD': {},
                            'Fiber Optic': {},
                            'SFP Modules': {},
                            'Patch Cords': {},
                        },
                    },
                    'Adapters & Cables': {
                        'children': {
                            'HDMI Cables': {},
                            'DisplayPort Cables': {},
                            'VGA Cables': {},
                            'USB Hubs': {},
                            'Docking Stations': {},
                            'USB Adapters': {},
                            'Thunderbolt Cables': {},
                            'Ethernet Cables': {},
                            'Fiber Patch Cords': {},
                            'Cable Management': {},
                        },
                    },
                    'Security Devices': {
                        'children': {
                            'Biometric Attendance': {},
                            'Fingerprint Scanners': {},
                            'Face Recognition': {},
                            'Access Control Systems': {},
                            'Metal Detectors': {},
                            'X-Ray Machines': {},
                            'Fire Alarm Systems': {},
                            'Emergency Lights': {},
                        },
                    },
                    'Televisions': {
                        'children': {
                            'Smart TVs': {},
                            'LED TVs': {},
                            'OLED TVs': {},
                            'QLED TVs': {},
                            '4K TVs': {},
                            'Android TVs': {},
                            'TV Wall Mounts': {},
                            'TV Stands': {},
                        },
                    },
                },
            },
        }

        created_count = 0
        updated_count = 0

        def create_category(name, data, parent=None, order=0):
            nonlocal created_count, updated_count
            cat, created = Category.objects.update_or_create(
                name=name,
                parent=parent,
                defaults={
                    'description': data.get('description', f'Buy {name} at best wholesale prices'),
                    'icon': data.get('icon', ''),
                    'sort_order': order,
                    'is_active': True,
                    'is_featured': data.get('is_featured', False),
                    'meta_title': data.get('meta_title', f'{name} - B2B Wholesale'),
                    'meta_description': data.get('meta_description', f'Shop {name} wholesale online. Best prices from verified sellers.'),
                },
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

            children = data.get('children', {})
            for idx, (child_name, child_data) in enumerate(children.items()):
                create_category(child_name, child_data, parent=cat, order=idx)

        for idx, (root_name, root_data) in enumerate(CATEGORY_TREE.items()):
            create_category(root_name, root_data, parent=None, order=idx)

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! Created: {created_count}, Updated: {updated_count}, '
            f'Total: {Category.objects.count()} categories\n'
        ))
