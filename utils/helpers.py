import uuid
import hashlib
from django.utils.text import slugify


def generate_uuid():
    return uuid.uuid4()


def generate_short_uuid():
    return uuid.uuid4().hex[:8]


def slugify_text(text):
    return slugify(text)


def mask_email(email):
    if not email or '@' not in email:
        return email
    local, domain = email.split('@')
    if len(local) <= 2:
        masked = local[0] + '*' * (len(local) - 1)
    else:
        masked = local[0] + '*' * (len(local) - 2) + local[-1]
    return f'{masked}@{domain}'


def mask_phone(phone):
    if not phone or len(phone) < 4:
        return phone
    return phone[:2] + '*' * (len(phone) - 4) + phone[-2:]


def hash_string(value):
    return hashlib.sha256(value.encode()).hexdigest()
