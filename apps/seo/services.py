from django.utils.text import slugify
from django.conf import settings
from django.db.models import Q, Count, Avg, F
from apps.categories.models import Category
from apps.brands.models import Brand
from apps.sellers.models import SellerProfile, SellerWarehouse
from apps.products.models import Product
from .models import SEOPage, SEOFAQ


INDIAN_CITIES = [
    'delhi', 'mumbai', 'bangalore', 'bengaluru', 'hyderabad', 'chennai',
    'kolkata', 'pune', 'ahmedabad', 'jaipur', 'lucknow', 'noida',
    'gurgaon', 'gurugram', 'faridabad', 'ghaziabad', 'meerut',
    'chandigarh', 'indore', 'bhopal', 'patna', 'ranchi', 'kochi',
    'coimbatore', 'madurai', 'visakhapatnam', 'nagpur', 'surat',
    'vadodara', 'rajkot', 'kanpur', 'agra', 'varanasi', 'dehradun',
    'mysore', 'thiruvananthapuram', 'goa', 'jodhpur', 'udaipur',
]

CITY_STATE_MAP = {
    'delhi': 'Delhi', 'noida': 'Uttar Pradesh', 'gurgaon': 'Haryana',
    'gurugram': 'Haryana', 'faridabad': 'Haryana', 'ghaziabad': 'Uttar Pradesh',
    'meerut': 'Uttar Pradesh', 'lucknow': 'Uttar Pradesh', 'agra': 'Uttar Pradesh',
    'varanasi': 'Uttar Pradesh', 'kanpur': 'Uttar Pradesh',
    'mumbai': 'Maharashtra', 'pune': 'Maharashtra', 'nagpur': 'Maharashtra',
    'surat': 'Gujarat', 'ahmedabad': 'Gujarat', 'vadodara': 'Gujarat',
    'rajkot': 'Gujarat',
    'bangalore': 'Karnataka', 'bengaluru': 'Karnataka', 'mysore': 'Karnataka',
    'hyderabad': 'Telangana',
    'chennai': 'Tamil Nadu', 'coimbatore': 'Tamil Nadu', 'madurai': 'Tamil Nadu',
    'kolkata': 'West Bengal',
    'jaipur': 'Rajasthan', 'jodhpur': 'Rajasthan', 'udaipur': 'Rajasthan',
    'chandigarh': 'Chandigarh',
    'indore': 'Madhya Pradesh', 'bhopal': 'Madhya Pradesh',
    'patna': 'Bihar', 'ranchi': 'Jharkhand',
    'kochi': 'Kerala', 'thiruvananthapuram': 'Kerala',
    'visakhapatnam': 'Andhra Pradesh',
    'dehradun': 'Uttarakhand',
    'goa': 'Goa',
}

SITE_NAME = 'B2B Market'


def build_heading(category=None, brand=None, city=None, keyword=None):
    """
    Build dynamic H1 heading and title based on available data.
    
    Examples:
        build_heading(category=Category('Laptops'), city='delhi')
        → heading: 'Wholesale Laptops in Delhi', title: 'Buy Wholesale Laptops in Delhi | B2B Market'
        
        build_heading(category=Category('Laptops'), brand=Brand('Dell'), city='delhi')
        → heading: 'Dell Laptops in Delhi', title: 'Buy Dell Laptops in Delhi | B2B Market'
        
        build_heading(keyword='cctv cameras', city='lucknow')
        → heading: 'CCTV Cameras in Lucknow', title: 'Buy CCTV Cameras in Lucknow | B2B Market'
    """
    parts = []
    if brand:
        parts.append(brand.name)
    if category:
        parts.append(category.name)
    elif keyword:
        parts.append(keyword.title())
    
    product_type = ' '.join(parts) if parts else 'Products'
    city_display = f' in {city.title()}' if city else ''
    
    # H1 heading
    if brand and category:
        heading = f'{brand.name} {category.name}{city_display}'
    elif category:
        heading = f'Wholesale {category.name}{city_display}'
    elif keyword:
        heading = f'{keyword.title()}{city_display}'
    else:
        heading = f'Wholesale {product_type}{city_display}'
    
    # Title tag (max 70 chars)
    title = f'Buy {product_type}{city_display} | {SITE_NAME}'
    if len(title) > 70:
        title = f'{product_type}{city_display} | {SITE_NAME}'
    if len(title) > 70:
        title = f'{product_type} | {SITE_NAME}'
    
    # Meta description (max 160 chars)
    meta_desc = f'Find wholesale {product_type.lower()} from verified sellers{city_display} with GST billing, bulk pricing and fast delivery.'
    if len(meta_desc) > 160:
        meta_desc = meta_desc[:157] + '...'
    
    return {
        'heading': heading,
        'title': title[:70],
        'meta_desc': meta_desc[:160],
        'product_type': product_type,
    }


def get_sellers_for_city(city):
    if not city:
        return SellerProfile.objects.filter(status='approved', is_verified=True)
    return SellerProfile.objects.filter(
        status='approved',
        warehouses__city__icontains=city,
        warehouses__is_active=True,
    ).distinct()


def get_products_for_seo(category=None, brand=None, city=None):
    qs = Product.objects.filter(is_active=True)
    if category:
        qs = qs.filter(Q(category=category) | Q(category__parent=category))
    if brand:
        qs = qs.filter(brand=brand)
    if city:
        qs = qs.filter(
            Q(seller__warehouses__city__icontains=city) &
            Q(seller__warehouses__is_active=True)
        ).distinct()
    return qs.select_related('category', 'brand', 'seller')


def generate_faq(category=None, brand=None, city=None):
    faqs = []
    cat_name = category.name if category else 'products'
    brand_name = brand.name if brand else ''
    loc = f' in {city.title()}' if city else ''
    seller_loc = f'{city.title()} ' if city else ''

    faqs.append({
        'question': f'What are the best wholesale {cat_name} suppliers{loc}?',
        'answer': f'You can find verified wholesale {cat_name} suppliers{loc} on our platform. All sellers are GST-verified with bulk pricing and fast delivery.',
    })
    faqs.append({
        'question': f'Do you provide GST invoices for {cat_name} purchases{loc}?',
        'answer': f'Yes, all our sellers provide proper GST invoices for every purchase. This helps with input tax credit and compliance.',
    })
    faqs.append({
        'question': f'What is the minimum order quantity for {cat_name}{loc}?',
        'answer': f'The minimum order quantity varies by seller and product. Most sellers offer MOQ starting from 1 piece. Contact sellers directly for bulk orders.',
    })
    faqs.append({
        'question': f'Can I buy {cat_name} in bulk{loc}?',
        'answer': f'Absolutely! Our platform specializes in B2B wholesale. You can buy {cat_name} in bulk with wholesale pricing and GST billing{loc}.',
    })
    if brand_name:
        faqs.append({
            'question': f'Which {brand_name} {cat_name} are available{loc}?',
            'answer': f'We have a wide range of {brand_name} {cat_name} available{loc}. Browse our catalog to see all available models and pricing.',
        })
    faqs.append({
        'question': f'Do you offer delivery for {cat_name} orders{loc}?',
        'answer': f'Yes, our sellers offer delivery across India including {city.title() if city else "all major cities"}. Delivery timelines depend on order size and location.',
    })
    return faqs


def generate_related_searches(category=None, brand=None, city=None):
    searches = []
    cat_slug = category.name.lower() if category else ''
    brand_name = brand.name.lower() if brand else ''
    loc = city.lower() if city else ''

    if cat_slug:
        if loc:
            searches.append(f'best {cat_slug} in {loc}')
            searches.append(f'wholesale {cat_slug} in {loc}')
            searches.append(f'{cat_slug} supplier in {loc}')
        else:
            searches.append(f'wholesale {cat_slug}')
            searches.append(f'buy {cat_slug} online')
    if brand_name and cat_slug:
        searches.append(f'{brand_name} {cat_slug}')
        if loc:
            searches.append(f'{brand_name} {cat_slug} in {loc}')
    if loc:
        searches.append(f'electronics wholesale in {loc}')
        searches.append(f'business supplies {loc}')
    return list(set(searches))[:12]


def generate_schema_json(page):
    schema = {
        '@context': 'https://schema.org',
        '@type': 'CollectionPage',
        'name': page.title,
        'description': page.meta_description,
        'url': page.canonical_url or f'{settings.SITE_URL}/{page.slug}',
    }
    if page.faq_json:
        schema['mainEntity'] = {
            '@type': 'FAQPage',
            'mainEntity': [
                {
                    '@type': 'Question',
                    'name': faq['question'],
                    'acceptedAnswer': {
                        '@type': 'Answer',
                        'text': faq['answer'],
                    }
                } for faq in page.faq_json
            ]
        }
    return schema


def generate_category_page(category, city=None):
    city_slug = slugify(city) if city else ''
    slug_parts = [category.slug]
    if city_slug:
        slug_parts.append(city_slug)
    slug = '/'.join(slug_parts)

    state = CITY_STATE_MAP.get(city.lower(), '') if city else ''
    seo = build_heading(category=category, city=city)
    city_display = f' in {city.title()}' if city else ''

    keywords = [
        f'{category.name.lower()} {city}'.strip(),
        f'wholesale {category.name.lower()}',
        f'bulk {category.name.lower()}',
        f'{category.name.lower()} supplier',
        f'{category.name.lower()} manufacturer',
    ]

    faqs = generate_faq(category=category, city=city)
    related = generate_related_searches(category=category, city=city)

    page, _ = SEOPage.objects.update_or_create(
        slug=slug,
        defaults={
            'page_type': 'category_city' if city else 'category',
            'category': category,
            'city': city or '',
            'state': state,
            'title': f'{slug.replace("/", " ").replace("-", " ").title()} | {SITE_NAME}'[:70],
            'meta_description': seo['meta_desc'],
            'meta_keywords': ', '.join(filter(None, keywords)),
            'h1_heading': slug.replace('-', ' ').replace('/', ' ').title(),
            'intro_text': f'Explore our wide range of {category.name.lower()} available{city_display}. Shop from verified sellers with competitive wholesale prices.',
            'buying_guide': f'When buying {category.name.lower()} in bulk, consider quality certifications, warranty terms, seller ratings, and delivery timelines. Our verified sellers ensure genuine products with GST invoicing.',
            'why_choose_us': f'Our platform connects you with verified {category.name.lower()} suppliers{city_display}. Enjoy bulk pricing, secure payments, and fast delivery across India.',
            'faq_json': faqs,
            'related_searches': related,
            'canonical_url': f'{settings.SITE_URL}/{slug}',
            'schema_json': generate_schema_json_with_faqs(seo['title'], seo['meta_desc'], faqs, f'{settings.SITE_URL}/{slug}'),
        }
    )

    if faqs:
        SEOFAQ.objects.filter(page=page).delete()
        for i, faq in enumerate(faqs):
            SEOFAQ.objects.create(page=page, question=faq['question'], answer=faq['answer'], sort_order=i)

    return page


def generate_category_brand_page(category, brand, city=None):
    city_slug = slugify(city) if city else ''
    slug_parts = [category.slug, brand.slug]
    if city_slug:
        slug_parts.append(city_slug)
    slug = '/'.join(slug_parts)

    state = CITY_STATE_MAP.get(city.lower(), '') if city else ''
    seo = build_heading(category=category, brand=brand, city=city)
    city_display = f' in {city.title()}' if city else ''

    keywords = [
        f'{brand.name.lower()} {category.name.lower()} {city}'.strip(),
        f'{brand.name.lower()} {category.name.lower()}',
        f'wholesale {brand.name.lower()} {category.name.lower()}',
        f'{brand.name.lower()} supplier',
    ]

    faqs = generate_faq(category=category, brand=brand, city=city)
    related = generate_related_searches(category=category, brand=brand, city=city)

    page, _ = SEOPage.objects.update_or_create(
        slug=slug,
        defaults={
            'page_type': 'category_brand_city' if city else 'category_brand',
            'category': category,
            'brand': brand,
            'city': city or '',
            'state': state,
            'title': f'{slug.replace("/", " ").replace("-", " ").title()} | {SITE_NAME}'[:70],
            'meta_description': seo['meta_desc'],
            'meta_keywords': ', '.join(filter(None, keywords)),
            'h1_heading': slug.replace('-', ' ').replace('/', ' ').title(),
            'intro_text': f'Explore {brand.name} {category.name.lower()} at wholesale prices{city_display}. Browse the complete range with bulk pricing from verified sellers.',
            'buying_guide': f'Choose genuine {brand.name} {category.name.lower()} from authorized sellers. Check warranty, GST invoice, and seller ratings before placing bulk orders.',
            'why_choose_us': f'We connect you with authorized {brand.name} sellers{city_display}. Get genuine products, wholesale pricing, and secure delivery.',
            'faq_json': faqs,
            'related_searches': related,
            'canonical_url': f'{settings.SITE_URL}/{slug}',
            'schema_json': generate_schema_json_with_faqs(f'{slug.replace("/", " ").replace("-", " ").title()} | {SITE_NAME}'[:70], seo['meta_desc'], faqs, f'{settings.SITE_URL}/{slug}'),
        }
    )

    if faqs:
        SEOFAQ.objects.filter(page=page).delete()
        for i, faq in enumerate(faqs):
            SEOFAQ.objects.create(page=page, question=faq['question'], answer=faq['answer'], sort_order=i)

    return page


def generate_brand_page(brand, city=None):
    city_slug = slugify(city) if city else ''
    slug_parts = [brand.slug]
    if city_slug:
        slug_parts.append(city_slug)
    slug = '/'.join(slug_parts)

    state = CITY_STATE_MAP.get(city.lower(), '') if city else ''
    seo = build_heading(brand=brand, city=city)
    city_display = f' in {city.title()}' if city else ''

    keywords = [
        f'{brand.name.lower()} {city}'.strip(),
        f'{brand.name.lower()} wholesale',
        f'{brand.name.lower()} supplier',
    ]

    faqs = generate_faq(brand=brand, city=city)
    related = generate_related_searches(brand=brand, city=city)

    page, _ = SEOPage.objects.update_or_create(
        slug=slug,
        defaults={
            'page_type': 'brand_city' if city else 'brand',
            'brand': brand,
            'city': city or '',
            'state': state,
            'title': f'{slug.replace("/", " ").replace("-", " ").title()} | {SITE_NAME}'[:70],
            'meta_description': seo['meta_desc'],
            'meta_keywords': ', '.join(filter(None, keywords)),
            'h1_heading': slug.replace('-', ' ').replace('/', ' ').title(),
            'intro_text': f'Explore the complete range of {brand.name} products{city_display}. Buy from verified sellers with wholesale pricing.',
            'faq_json': faqs,
            'related_searches': related,
            'canonical_url': f'{settings.SITE_URL}/{slug}',
            'schema_json': generate_schema_json_with_faqs(f'{slug.replace("/", " ").replace("-", " ").title()} | {SITE_NAME}'[:70], seo['meta_desc'], faqs, f'{settings.SITE_URL}/{slug}'),
        }
    )
    return page


def generate_all_seo_pages():
    categories = Category.objects.filter(is_active=True, parent__isnull=True)
    brands = Brand.objects.filter(is_active=True)
    cities = INDIAN_CITIES

    count = 0
    for cat in categories:
        generate_category_page(cat)
        count += 1
        for city in cities:
            generate_category_page(cat, city)
            count += 1

        for brand in brands:
            generate_category_brand_page(cat, brand)
            count += 1
            for city in cities:
                generate_category_brand_page(cat, brand, city)
                count += 1

    for brand in brands:
        generate_brand_page(brand)
        count += 1
        for city in cities:
            generate_brand_page(brand, city)
            count += 1

    return count


def generate_schema_json_with_faqs(title, description, faqs, url):
    schema = {
        '@context': 'https://schema.org',
        '@type': 'CollectionPage',
        'name': title,
        'description': description,
        'url': url,
    }
    if faqs:
        schema['mainEntity'] = {
            '@type': 'FAQPage',
            'mainEntity': [
                {
                    '@type': 'Question',
                    'name': faq['question'],
                    'acceptedAnswer': {
                        '@type': 'Answer',
                        'text': faq['answer'],
                    }
                } for faq in faqs
            ]
        }
    return schema
