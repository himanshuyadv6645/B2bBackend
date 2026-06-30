import cloudinary
import cloudinary.uploader
from django.conf import settings


_cloudinary_configured = False


def _ensure_cloudinary_config():
    global _cloudinary_configured
    if not _cloudinary_configured:
        storage = getattr(settings, 'CLOUDINARY_STORAGE', {})
        cloudinary.config(
            cloud_name=storage.get('CLOUD_NAME', ''),
            api_key=storage.get('API_KEY', ''),
            api_secret=storage.get('API_SECRET', ''),
            secure=True,
        )
        _cloudinary_configured = True


def upload_image(file, folder='b2bmarketplace', transformation=None):
    try:
        _ensure_cloudinary_config()
        result = cloudinary.uploader.upload(
            file,
            folder=folder,
            resource_type='image',
            transformation=transformation or [
                {'quality': 'auto', 'fetch_format': 'auto'},
            ],
        )
        return {
            'url': result.get('secure_url'),
            'public_id': result.get('public_id'),
            'width': result.get('width'),
            'height': result.get('height'),
            'format': result.get('format'),
        }
    except Exception as e:
        return {'error': str(e)}


def upload_file(file, folder='b2bmarketplace/documents'):
    try:
        _ensure_cloudinary_config()
        result = cloudinary.uploader.upload(
            file,
            folder=folder,
            resource_type='raw',
        )
        return {
            'url': result.get('secure_url'),
            'public_id': result.get('public_id'),
            'format': result.get('format'),
        }
    except Exception as e:
        return {'error': str(e)}


def delete_file(public_id):
    try:
        _ensure_cloudinary_config()
        result = cloudinary.uploader.destroy(public_id)
        return result
    except Exception as e:
        return {'error': str(e)}
