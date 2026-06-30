import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Q, F
from django.conf import settings
from django.http import HttpResponse
from apps.categories.models import Category
from apps.brands.models import Brand
from apps.sellers.models import SellerProfile
from apps.products.models import Product
from .models import SEOPage
from .serializers import SEOPageDetailSerializer
from .services import (
    generate_category_page, generate_category_brand_page,
    generate_brand_page, get_sellers_for_city, INDIAN_CITIES,
    build_heading, SITE_NAME,
)

# Words to strip from search slugs
FILLER_WORDS = {
    'wholesale', 'best', 'buy', 'top', 'supplier', 'suppliers',
    'manufacturer', 'manufacturers', 'dealer', 'dealers', 'price',
    'prices', 'online', 'shop', 'store', 'store', 'in', 'at',
    'the', 'for', 'and', 'or', 'with', 'from', 'all', 'new',
    'used', 'cheap', 'affordable', 'premium', 'quality',
}


def parse_seo_slug(slug):
    """
    Parse a slug like 'wholesale-laptops-in-delhi' into:
    keyword='laptops', city='delhi'
    
    Or 'dell-laptops-in-noida' into:
    brand='dell', keyword='laptops', city='noida'
    
    Or 'best-cctv-camera-suppliers-in-lucknow' into:
    keyword='cctv camera', city='lucknow'
    """
    words = slug.replace('-', ' ').lower().split()
    city = None
    brand = None
    keyword_parts = []

    # 1. Extract city from end
    for i in range(len(words) - 1, -1, -1):
        if words[i] in INDIAN_CITIES:
            city = words[i]
            words = words[:i]
            break

    # 2. Check if first word is a brand
    if words:
        first_brand = Brand.objects.filter(
            Q(slug=words[0]) | Q(name__iexact=words[0]),
            is_active=True
        ).first()
        if first_brand:
            brand = first_brand
            words = words[1:]

    # 3. Check remaining words for brand
    if not brand and words:
        for i, word in enumerate(words):
            b = Brand.objects.filter(
                Q(slug=word) | Q(name__iexact=word),
                is_active=True
            ).first()
            if b:
                brand = b
                words = words[:i] + words[i+1:]
                break

    # 4. Remove filler words, keep keyword parts
    for word in words:
        if word not in FILLER_WORDS and len(word) > 1:
            keyword_parts.append(word)

    keyword = ' '.join(keyword_parts) if keyword_parts else None

    return keyword, brand, city


def match_category_from_keyword(keyword):
    """Match a keyword to a category using multiple strategies."""
    if not keyword:
        return None

    # Direct slug match
    cat = Category.objects.filter(slug=keyword.replace(' ', '-'), is_active=True).first()
    if cat:
        return cat

    # Exact name match
    cat = Category.objects.filter(name__iexact=keyword, is_active=True).first()
    if cat:
        return cat

    # Contains match (prefer higher level categories)
    cat = Category.objects.filter(
        Q(name__icontains=keyword) | Q(slug__icontains=keyword.replace(' ', '-')),
        is_active=True
    ).order_by('level', 'sort_order').first()
    if cat:
        return cat

    # Keywords/aliases match (handles misspellings)
    cat = Category.objects.filter(
        Q(keywords__icontains=keyword),
        is_active=True,
    ).order_by('level', 'sort_order').first()
    if cat:
        return cat

    # Word-level match
    words = keyword.split()
    for word in words:
        if len(word) < 3:
            continue
        cat = Category.objects.filter(
            Q(name__icontains=word) | Q(slug__icontains=word) | Q(keywords__icontains=word),
            is_active=True
        ).order_by('level', 'sort_order').first()
        if cat:
            return cat

    return None


class SEOResolveView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, path=''):
        path = path.strip('/')
        if not path:
            return Response({'error': 'Path required'}, status=400)

        # 1. Check cached SEO page
        page = SEOPage.objects.filter(slug=path, is_active=True).first()
        if page:
            return self._build_response(page, path)

        # 2. Try structured path: category/brand/city
        page = self._try_structured_path(path)
        if page:
            return self._build_response(page, path)

        # 3. Try keyword search: wholesale-laptops-in-delhi
        page = self._try_keyword_search(path)
        if page:
            return self._build_response(page, path)

        # 4. Last resort: show all products
        page = self._create_fallback_page(path)
        if page:
            return self._build_response(page, path)

        return Response({'error': 'Page not found'}, status=404)

    def _build_response(self, page, path, keyword=None):
        SEOPage.objects.filter(pk=page.pk).update(views_count=F('views_count') + 1)
        serializer = SEOPageDetailSerializer(page)
        data = serializer.data
        # If no keyword passed, extract from slug
        if not keyword and not page.category and not page.brand:
            kw, _, _ = parse_seo_slug(path)
            keyword = kw
        data['products'] = self._get_products(page, keyword)
        data['sellers'] = self._get_sellers(page)
        data['breadcrumbs'] = self._get_breadcrumbs(page)
        data['related_categories'] = self._get_related_categories(page)
        data['total_products'] = len(data['products'])
        return Response(data)

    def _try_structured_path(self, path):
        """Handle paths like: laptops, laptops/dell, laptops/dell/delhi"""
        parts = [p for p in path.split('/') if p]
        if not parts:
            return None

        category = None
        brand = None
        city = None

        # First part = category
        if parts[0]:
            category = Category.objects.filter(
                Q(slug=parts[0]) | Q(name__iexact=parts[0].replace('-', ' ')),
                is_active=True
            ).first()

        # Second part = brand or city
        if len(parts) > 1 and parts[1]:
            brand = Brand.objects.filter(
                Q(slug=parts[1]) | Q(name__iexact=parts[1].replace('-', ' ')),
                is_active=True
            ).first()
            if not brand and parts[1].lower() in INDIAN_CITIES:
                city = parts[1].lower()

        # Third part = city or brand
        if len(parts) > 2 and parts[2]:
            if not city and parts[2].lower() in INDIAN_CITIES:
                city = parts[2].lower()
            elif not brand:
                brand = Brand.objects.filter(
                    Q(slug=parts[2]) | Q(name__iexact=parts[2].replace('-', ' ')),
                    is_active=True
                ).first()

        # Fourth part = city
        if len(parts) > 3 and parts[3] and not city:
            if parts[3].lower() in INDIAN_CITIES:
                city = parts[3].lower()

        if category:
            if brand:
                return generate_category_brand_page(category, brand, city)
            return generate_category_page(category, city)

        if brand:
            return generate_brand_page(brand, city)

        return None

    def _try_keyword_search(self, path):
        """Handle paths like: wholesale-laptops-in-delhi, best-cctv-cameras"""
        keyword, brand, city = parse_seo_slug(path)

        # If no keyword found after parsing, try the raw slug
        if not keyword and not brand:
            # Check if the raw slug matches anything
            cat = Category.objects.filter(
                Q(slug=path) | Q(name__iexact=path.replace('-', ' ')),
                is_active=True
            ).first()
            if cat:
                return generate_category_page(cat, city)

            brand_obj = Brand.objects.filter(
                Q(slug=path) | Q(name__iexact=path.replace('-', ' ')),
                is_active=True
            ).first()
            if brand_obj:
                return generate_brand_page(brand_obj, city)

            return None

        # Match keyword to category
        category = match_category_from_keyword(keyword) if keyword else None

        if category and brand:
            return generate_category_brand_page(category, brand, city)
        elif category:
            return self._create_search_page(path, keyword, city, category=category)
        elif brand:
            return generate_brand_page(brand, city)

        # No category or brand matched - create search page
        return self._create_search_page(path, keyword, city)

    def _create_search_page(self, slug, keyword, city=None, category=None):
        title_words = (keyword or slug).replace('-', ' ').title()
        slug_heading = slug.replace('-', ' ').replace('/', ' ').title()
        city_display = f' in {city.title()}' if city else ''

        faqs = [
            {'question': f'What are the best {title_words} suppliers{city_display}?',
             'answer': f'Find verified {title_words.lower()} suppliers{city_display} on our platform with GST billing and bulk pricing.'},
            {'question': f'Do you provide GST invoices?',
             'answer': 'Yes, all sellers provide proper GST invoices for every purchase.'},
            {'question': f'Can I buy {title_words.lower()} in bulk?',
             'answer': 'Absolutely! Our platform specializes in B2B wholesale with competitive pricing.'},
        ]

        page, _ = SEOPage.objects.update_or_create(
            slug=slug,
            defaults={
                'page_type': 'search',
                'category': category,
                'city': city or '',
                'title': f'{slug_heading} | {SITE_NAME}'[:70],
                'meta_description': f'Buy {title_words.lower()}{city_display} at wholesale prices. Verified sellers, GST billing.'[:160],
                'h1_heading': slug_heading,
                'intro_text': f'Explore {title_words.lower()} at wholesale prices{city_display}. Browse from verified sellers with GST invoicing.',
                'buying_guide': f'When buying {title_words.lower()} in bulk, consider quality, warranty, seller ratings, and delivery timelines.',
                'why_choose_us': f'Our platform connects you with verified {title_words.lower()} suppliers{city_display}. Enjoy bulk pricing, secure payments, and fast delivery.',
                'faq_json': faqs,
                'related_searches': self._build_related_searches(title_words, city),
                'canonical_url': f'{settings.SITE_URL}/{slug}',
            }
        )
        return page

    def _build_related_searches(self, keyword, city=None):
        kw = keyword.lower()
        searches = []
        if city:
            c = city.lower()
            searches.extend([
                f'wholesale {kw} in {c}',
                f'{kw} price in {c}',
                f'buy {kw} online in {c}',
                f'{kw} supplier in {c}',
                f'best {kw} in {c}',
            ])
        else:
            searches.extend([
                f'wholesale {kw}',
                f'{kw} price',
                f'buy {kw} online',
                f'{kw} supplier',
            ])
        return list(dict.fromkeys(searches))[:10]

    def _create_fallback_page(self, path):
        _, _, city = parse_seo_slug(path)
        slug_heading = path.replace('-', ' ').replace('/', ' ').title()
        words = path.replace('-', ' ').replace('/', ' ').title()
        city_display = f' in {city.title()}' if city else ''
        faqs = [
            {'question': f'What are the best {words.lower()} suppliers{city_display}?',
             'answer': f'Find verified {words.lower()} suppliers{city_display} on our platform with GST billing and bulk pricing.'},
            {'question': 'Do you provide GST invoices?',
             'answer': 'Yes, all sellers provide proper GST invoices for every purchase.'},
        ]
        page, _ = SEOPage.objects.update_or_create(
            slug=path,
            defaults={
                'page_type': 'search',
                'city': city or '',
                'title': f'{slug_heading} | {SITE_NAME}'[:70],
                'meta_description': f'Buy {words.lower()}{city_display} at wholesale prices. Verified sellers, GST billing.'[:160],
                'h1_heading': slug_heading,
                'intro_text': f'Explore {words.lower()} at wholesale prices{city_display}. Browse from verified sellers.',
                'faq_json': faqs,
                'related_searches': self._build_related_searches(words.lower(), city),
                'canonical_url': f'{settings.SITE_URL}/{path}',
            }
        )
        return page

    def _get_products(self, page, keyword=None):
        qs = Product.objects.filter(is_active=True, deleted_at__isnull=True)
        has_filter = False

        if page.category:
            cat_ids = [page.category.id]
            children = Category.objects.filter(parent=page.category, is_active=True).values_list('id', flat=True)
            cat_ids.extend(children)
            qs = qs.filter(category_id__in=cat_ids)
            has_filter = True

        if page.brand:
            qs = qs.filter(brand=page.brand)
            has_filter = True

        # Keyword filter: search product name when no category/brand matched
        if keyword and not has_filter:
            qs = qs.filter(
                Q(name__icontains=keyword) |
                Q(description__icontains=keyword) |
                Q(category__name__icontains=keyword)
            )
            has_filter = True

        if page.city:
            # City filter: only filter if products actually have sellers with warehouses
            city_products = qs.filter(
                Q(seller__warehouses__city__icontains=page.city) &
                Q(seller__warehouses__is_active=True)
            ).distinct()
            # Use city-filtered products if any exist, otherwise fallback to all matching
            if city_products.exists():
                qs = city_products
            has_filter = True

        if not has_filter:
            qs = qs.order_by('-is_featured', '-is_trending', '-average_rating')

        products = qs.select_related('category', 'brand', 'seller').prefetch_related('images')[:48]
        result = []
        for p in products:
            img = p.images.filter(is_primary=True).first() or p.images.first()
            discount = 0
            try:
                mrp = float(getattr(p, 'max_mrp', p.retail_price) or p.retail_price or 0)
                price = float(p.min_selling_price or 0)
                if mrp > 0 and price > 0 and mrp > price:
                    discount = round((1 - price / mrp) * 100)
            except (ValueError, TypeError):
                pass
            result.append({
                'id': str(p.id),
                'name': p.name,
                'slug': p.slug,
                'min_selling_price': str(p.min_selling_price),
                'max_selling_price': str(p.max_selling_price),
                'retail_price': str(p.retail_price),
                'min_mrp': str(getattr(p, 'min_mrp', p.retail_price)),
                'max_mrp': str(getattr(p, 'max_mrp', p.retail_price)),
                'average_rating': str(p.average_rating),
                'total_reviews': p.total_reviews,
                'total_stock': p.total_stock,
                'total_sellers': getattr(p, 'total_sellers', 0),
                'moq': p.moq,
                'is_active': True,
                'is_featured': p.is_featured,
                'is_trending': getattr(p, 'is_trending', False),
                'is_top_seller': getattr(p, 'is_top_seller', False),
                'primary_image': img.image_url if img else '',
                'category': str(p.category.id) if p.category else '',
                'category_name': p.category.name if p.category else '',
                'category_slug': p.category.slug if p.category else '',
                'brand': str(p.brand.id) if p.brand else '',
                'brand_name': p.brand.name if p.brand else '',
                'brand_slug': p.brand.slug if p.brand else '',
                'seller_name': p.seller.company_name if p.seller else '',
                'discount_percent': discount,
                'short_description': getattr(p, 'short_description', ''),
                'sku': getattr(p, 'sku', ''),
                'moq': p.moq,
                'gst': str(getattr(p, 'gst', '18')),
                'warranty': getattr(p, 'warranty', ''),
                'country_of_origin': getattr(p, 'country_of_origin', 'India'),
                'hsn_code': getattr(p, 'hsn_code', ''),
            })
        return result

    def _get_sellers(self, page):
        if not page.city:
            return []
        sellers = get_sellers_for_city(page.city).select_related('user')[:12]
        return [
            {
                'id': str(s.id),
                'company_name': s.company_name,
                'logo': s.logo or '',
                'rating': str(s.rating),
                'total_ratings': s.total_ratings,
                'is_verified': s.is_verified,
                'city': s.warehouses.filter(is_primary=True).first().city if s.warehouses.exists() else '',
            }
            for s in sellers
        ]

    def _get_breadcrumbs(self, page):
        crumbs = [{'name': 'Home', 'url': '/'}]
        if page.category:
            crumbs.append({'name': page.category.name, 'url': f'/categories/{page.category.slug}'})
            if page.brand:
                crumbs.append({'name': page.brand.name, 'url': None})
        elif page.brand:
            crumbs.append({'name': page.brand.name, 'url': None})
        if page.city:
            crumbs.append({'name': page.city.title(), 'url': None})
        return crumbs

    def _get_related_categories(self, page):
        if page.category:
            siblings = Category.objects.filter(
                parent=page.category.parent, is_active=True
            ).exclude(id=page.category.id)[:8]
            return [{'name': c.name, 'slug': c.slug, 'image': c.image or ''} for c in siblings]
        return [{'name': c.name, 'slug': c.slug, 'image': c.image or ''}
                for c in Category.objects.filter(is_active=True, parent__isnull=True)[:8]]


class SEOGenerateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        from .services import generate_all_seo_pages
        count = generate_all_seo_pages()
        return Response({'message': f'Generated {count} SEO pages', 'count': count})


class SEOSitemapView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        base = f'{settings.SITE_URL}'
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        xml += f'  <url><loc>{base}/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>\n'
        for slug in Product.objects.filter(is_active=True).values_list('slug', flat=True):
            xml += f'  <url><loc>{base}/products/{slug}</loc><changefreq>weekly</changefreq><priority>0.9</priority></url>\n'
        for slug in Category.objects.filter(is_active=True).values_list('slug', flat=True):
            xml += f'  <url><loc>{base}/categories/{slug}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
        for slug in Brand.objects.filter(is_active=True).values_list('slug', flat=True):
            xml += f'  <url><loc>{base}/brands/{slug}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
        for slug in SEOPage.objects.filter(is_active=True).values_list('slug', flat=True):
            xml += f'  <url><loc>{base}/{slug}</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>\n'
        xml += '</urlset>'
        return HttpResponse(xml, content_type='application/xml')


class SEORobotsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        robots = f"User-agent: *\nAllow: /\nDisallow: /api/\nDisallow: /admin/\nDisallow: /seller/\nDisallow: /buyer/\n\nSitemap: {settings.SITE_URL}/api/v1/seo/sitemap.xml\n"
        return HttpResponse(robots, content_type='text/plain')
