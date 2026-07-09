import uuid
from django.db import models


class AnalyticsEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        'authentication.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    event_type = models.CharField(max_length=100, db_index=True)
    entity_type = models.CharField(max_length=50, blank=True, null=True)
    entity_id = models.UUIDField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=500, blank=True, null=True)
    session_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'analytics_events'
        verbose_name = 'Analytics Event'
        verbose_name_plural = 'Analytics Events'
        ordering = ['-created_at']
        indexes = [
            # Per-user behaviour timelines (most-viewed, recent activity).
            models.Index(
                fields=['user', 'event_type', '-created_at'],
                name='ae_user_event_created_idx',
            ),
            # Popularity / entity roll-ups (most-viewed product across users).
            models.Index(
                fields=['entity_type', 'entity_id', 'event_type'],
                name='ae_entity_event_idx',
            ),
            # Abandoned cart/checkout scans over a recent time window.
            models.Index(
                fields=['event_type', '-created_at'],
                name='ae_event_created_idx',
            ),
        ]

    def __str__(self):
        return f'{self.event_type} - {self.entity_type or ""} {self.entity_id or ""}'
