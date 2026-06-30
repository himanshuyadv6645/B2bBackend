from django.core.exceptions import ValidationError


def validate_image_file(file):
    valid_types = ['image/jpeg', 'image/png', 'image/webp', 'image/gif']
    max_size = 5 * 1024 * 1024  # 5MB

    if file.content_type not in valid_types:
        raise ValidationError('Only JPEG, PNG, WebP, and GIF images are allowed.')

    if file.size > max_size:
        raise ValidationError('Image size must be less than 5MB.')


def validate_document_file(file):
    valid_types = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    ]
    max_size = 10 * 1024 * 1024  # 10MB

    if file.content_type not in valid_types:
        raise ValidationError('Only PDF and DOC files are allowed.')

    if file.size > max_size:
        raise ValidationError('File size must be less than 10MB.')
