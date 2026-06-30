import uuid
from django.utils.text import slugify


def generate_unique_slug(instance, value, slug_field='slug', new_id=None):
    slug = slugify(value)
    if new_id is None:
        new_id = uuid.uuid4().hex[:8]
    unique_slug = f'{slug}-{new_id}'

    ModelClass = instance.__class__
    while ModelClass.objects.filter(**{slug_field: unique_slug}).exists():
        new_id = uuid.uuid4().hex[:8]
        unique_slug = f'{slug}-{new_id}'

    return unique_slug


def generate_order_number():
    import random
    import string
    from django.utils import timezone

    now = timezone.now()
    year = now.strftime('%Y')
    random_digits = ''.join(random.choices(string.digits, k=6))
    return f'ORD-{year}-{random_digits}'


def generate_invoice_number():
    import random
    import string
    from django.utils import timezone

    now = timezone.now()
    year = now.strftime('%Y')
    random_digits = ''.join(random.choices(string.digits, k=6))
    return f'INV-{year}-{random_digits}'
