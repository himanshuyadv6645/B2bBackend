import logging

from django.conf import settings

from apps.notifications.models import Notification, DeviceToken

logger = logging.getLogger(__name__)


class NotificationService:
    @staticmethod
    def create_notification(user, notification_type, title, message, reference_type=None, reference_id=None, action_url=None, send_push=True, push_data=None):
        notification = Notification.objects.create(
            user=user,
            notification_type=notification_type,
            title=title,
            message=message,
            reference_type=reference_type,
            reference_id=reference_id,
            action_url=action_url,
        )
        if send_push:
            # Best-effort: a push failure must never break the in-app notification.
            try:
                data = {
                    'notification_id': str(notification.id),
                    'notification_type': notification_type or '',
                    'action_url': action_url or '',
                    'reference_type': reference_type or '',
                    'reference_id': str(reference_id) if reference_id else '',
                }
                # Optional rich-push fields (e.g. image_url, button_text) that the
                # service worker understands.
                if push_data:
                    data.update({k: v for k, v in push_data.items() if v is not None})
                PushService.send_to_user(user, title=title, body=message, data=data)
            except Exception as exc:  # noqa: BLE001
                logger.warning('Push send failed for notification %s: %s', notification.id, exc)
        return notification

    @staticmethod
    def get_notifications(user, unread_only=False):
        queryset = Notification.objects.filter(user=user)
        if unread_only:
            queryset = queryset.filter(is_read=False)
        return queryset

    @staticmethod
    def mark_as_read(notification_id, user):
        try:
            notification = Notification.objects.get(id=notification_id, user=user)
            notification.mark_as_read()
            return True
        except Notification.DoesNotExist:
            return False

    @staticmethod
    def mark_all_as_read(user):
        Notification.objects.filter(user=user, is_read=False).update(is_read=True)
        return True

    @staticmethod
    def get_unread_count(user):
        return Notification.objects.filter(user=user, is_read=False).count()

    @staticmethod
    def delete_notification(notification_id, user):
        deleted, _ = Notification.objects.filter(id=notification_id, user=user).delete()
        return deleted > 0


class PushService:
    """Sends FCM push messages and manages device tokens.

    Everything here degrades gracefully: if Firebase is not configured, sends
    are skipped and registration still stores tokens (so push starts working the
    moment credentials are added, without users having to re-register).
    """

    @staticmethod
    def register_device(user, token, platform='web', user_agent=None):
        """Store/refresh an FCM token for this user. Reassigns if it moved users."""
        obj, _ = DeviceToken.objects.update_or_create(
            token=token,
            defaults={
                'user': user,
                'platform': platform or 'web',
                'user_agent': (user_agent or '')[:500] or None,
                'is_active': True,
            },
        )
        return obj

    @staticmethod
    def unregister_device(token):
        """Remove a token (called on logout / when it becomes invalid)."""
        deleted, _ = DeviceToken.objects.filter(token=token).delete()
        return deleted > 0

    @staticmethod
    def send_to_user(user, title, body, data=None):
        """Send a push to every active token of `user`. Prunes dead tokens.

        Returns the number of messages successfully sent (0 if push disabled).
        """
        from apps.notifications.fcm import get_app

        app = get_app()
        if app is None:
            return 0

        tokens = list(
            DeviceToken.objects.filter(user=user, is_active=True)
            .values_list('token', flat=True)
        )
        if not tokens:
            return 0

        return PushService._send(app, tokens, title, body, data or {})

    @staticmethod
    def broadcast(title, body, data=None):
        """Send a push to all active tokens."""
        from apps.notifications.fcm import get_app
        app = get_app()
        if app is None:
            return 0
            
        tokens = list(DeviceToken.objects.filter(is_active=True).values_list('token', flat=True))
        if not tokens:
            return 0
            
        return PushService._send(app, tokens, title, body, data or {})

    @staticmethod
    def _absolute_link(action_url):
        """Return an absolute HTTPS URL for FCM's webpush link, or None."""
        if not action_url:
            return None
        if action_url.startswith('https://'):
            return action_url
        if action_url.startswith('http://'):
            return None
        base = (getattr(settings, 'SITE_URL', '') or '').rstrip('/')
        if action_url.startswith('/') and base.startswith('https://'):
            return base + action_url
        return None

    @staticmethod
    def _send(app, tokens, title, body, data):
        from firebase_admin import messaging

        str_data = {k: ('' if v is None else str(v)) for k, v in data.items()}

        webpush_kwargs = {
            'notification': messaging.WebpushNotification(
                title=title, body=body, icon='/favicon.svg',
                image=str_data.get('image_url') if str_data.get('image_url') else None,
            ),
        }
        link = PushService._absolute_link(str_data.get('action_url'))
        if link:
            webpush_kwargs['fcm_options'] = messaging.WebpushFCMOptions(link=link)

        # Firebase multicast has a limit of 500 tokens per request
        chunk_size = 500
        total_success = 0
        stale = []

        for i in range(0, len(tokens), chunk_size):
            chunk_tokens = tokens[i:i + chunk_size]
            message = messaging.MulticastMessage(
                tokens=chunk_tokens,
                notification=messaging.Notification(title=title, body=body),
                data=str_data,
                webpush=messaging.WebpushConfig(**webpush_kwargs),
            )

            try:
                response = messaging.send_each_for_multicast(message, app=app)
                total_success += response.success_count
                
                # Prune tokens FCM reports as unregistered / invalid.
                for token, resp in zip(chunk_tokens, response.responses):
                    if resp.success:
                        continue
                    err = getattr(resp, 'exception', None)
                    code = getattr(err, 'code', '') or ''
                    if any(s in str(code).lower() for s in ('not-registered', 'invalid-argument', 'unregistered')):
                        stale.append(token)
            except Exception as exc:  # noqa: BLE001
                logger.warning('FCM multicast failed: %s', exc)

        if stale:
            DeviceToken.objects.filter(token__in=stale).delete()

        return total_success
