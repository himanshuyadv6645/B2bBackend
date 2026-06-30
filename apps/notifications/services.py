from apps.notifications.models import Notification


class NotificationService:
    @staticmethod
    def create_notification(user, notification_type, title, message, reference_type=None, reference_id=None, action_url=None):
        notification = Notification.objects.create(
            user=user,
            notification_type=notification_type,
            title=title,
            message=message,
            reference_type=reference_type,
            reference_id=reference_id,
            action_url=action_url,
        )
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
