import uuid
from django.db import models


class Notification(models.Model):
    TYPE_CHOICES = (
        ('order', 'Order'),
        ('promotion', 'Promotion'),
        ('system', 'System'),
        ('seller', 'Seller'),
        ('review', 'Review'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='notifications',
    )
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    message = models.TextField()
    reference_type = models.CharField(max_length=50, blank=True, null=True)
    reference_id = models.UUIDField(blank=True, null=True)
    action_url = models.URLField(max_length=500, blank=True, null=True)
    is_read = models.BooleanField(default=False)
    is_sent_email = models.BooleanField(default=False)
    is_sent_sms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} - {self.user.email}'

    def mark_as_read(self):
        self.is_read = True
        self.save(update_fields=['is_read'])


class DeviceToken(models.Model):
    """An FCM registration token for one of a user's devices/browsers.

    One user can have many tokens (multiple browsers/devices). A token is unique
    globally; if it re-registers under a different user we reassign it.
    """
    PLATFORM_CHOICES = (
        ('web', 'Web'),
        ('android', 'Android'),
        ('ios', 'iOS'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='device_tokens',
    )
    token = models.TextField(unique=True)
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES, default='web')
    user_agent = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'device_tokens'
        verbose_name = 'Device Token'
        verbose_name_plural = 'Device Tokens'
        ordering = ['-last_used_at']
        indexes = [
            models.Index(fields=['user', 'is_active'], name='dt_user_active_idx'),
        ]

    def __str__(self):
        return f'{self.platform} token for {self.user_id}'


class NotificationTemplate(models.Model):
    TYPE_CHOICES = (
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('in_app', 'In-App'),
        ('push', 'Push'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    template_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body_template = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notification_templates'
        verbose_name = 'Notification Template'
        verbose_name_plural = 'Notification Templates'

    def __str__(self):
        return f'{self.name} ({self.template_type})'
