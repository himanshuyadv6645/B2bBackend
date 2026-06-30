import re
from django.core.exceptions import ValidationError


def validate_gstin(value):
    if not value:
        return
    pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid GSTIN format.')


def validate_pan(value):
    if not value:
        return
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if not re.match(pattern, value):
        raise ValidationError('Invalid PAN format.')


def validate_pincode(value):
    if not re.match(r'^[1-9][0-9]{5}$', value):
        raise ValidationError('Invalid Indian pincode.')


def validate_phone(value):
    if not re.match(r'^[6-9]\d{9}$', value):
        raise ValidationError('Invalid Indian phone number.')


def validate_seller_pricing(value):
    if value < 0:
        raise ValidationError('Price cannot be negative.')


def validate_rating(value):
    if not (1 <= value <= 5):
        raise ValidationError('Rating must be between 1 and 5.')


def sanitize_string(value):
    if not value:
        return value
    value = value.strip()
    value = re.sub(r'<[^>]+>', '', value)
    return value
