from django.contrib import admin
from .models import AnalyticsEvent


@admin.register(AnalyticsEvent)
class AnalyticsEventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'entity_type', 'entity_id', 'user', 'created_at')
    list_filter = ('event_type', 'entity_type')
    search_fields = ('event_type',)
