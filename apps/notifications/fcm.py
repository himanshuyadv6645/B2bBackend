"""Firebase Cloud Messaging bootstrap.

Initialises the firebase-admin app exactly once, lazily, from credentials in
settings. If no credentials are configured (local dev without Firebase, or a
deploy that hasn't set them yet), this stays disabled and every push call
becomes a no-op — in-app notifications keep working regardless.

Credentials come from settings, in this order:
  1. FIREBASE_CREDENTIALS_JSON  - raw service-account JSON string
  2. FIREBASE_CREDENTIALS_FILE  - path to the service-account .json
"""
import json
import logging
import threading

from django.conf import settings

logger = logging.getLogger(__name__)

_lock = threading.Lock()
_app = None
_initialised = False


def _load_credentials():
    """Return a firebase_admin.credentials.Certificate or None."""
    from firebase_admin import credentials

    raw = (settings.FIREBASE_CREDENTIALS_JSON or '').strip()
    if raw:
        try:
            return credentials.Certificate(json.loads(raw))
        except (ValueError, json.JSONDecodeError) as exc:
            logger.error('FIREBASE_CREDENTIALS_JSON is not valid JSON: %s', exc)
            return None

    path = (settings.FIREBASE_CREDENTIALS_FILE or '').strip()
    if path:
        try:
            return credentials.Certificate(path)
        except (IOError, ValueError) as exc:
            logger.error('FIREBASE_CREDENTIALS_FILE could not be loaded: %s', exc)
            return None

    return None


def get_app():
    """Return the initialised firebase app, or None if push is not configured."""
    global _app, _initialised

    if _initialised:
        return _app

    with _lock:
        if _initialised:
            return _app
        _initialised = True

        try:
            import firebase_admin
        except ImportError:
            logger.warning('firebase-admin is not installed; push disabled.')
            _app = None
            return None

        cred = _load_credentials()
        if cred is None:
            logger.info('Firebase credentials not configured; push disabled.')
            _app = None
            return None

        try:
            _app = firebase_admin.initialize_app(cred)
            logger.info('Firebase initialised; push enabled.')
        except Exception as exc:  # noqa: BLE001 - never let init crash the app
            logger.error('Firebase initialise failed: %s', exc)
            _app = None

        return _app


def is_enabled():
    return get_app() is not None
