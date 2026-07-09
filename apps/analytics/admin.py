from django.contrib import admin
from .models import AnalyticsEvent


@admin.register(AnalyticsEvent)
class AnalyticsEventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'entity_type', 'entity_id', 'user', 'created_at')
    list_filter = ('event_type', 'entity_type', 'created_at')
    search_fields = ('event_type', 'entity_id', 'user__email', 'session_id')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 50
    list_select_related = ('user',)
    readonly_fields = (
        'id', 'user', 'event_type', 'entity_type', 'entity_id',
        'metadata', 'ip_address', 'user_agent', 'session_id', 'created_at',
    )

    # Analytics events are an immutable log: view them, don't edit/create them.
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
