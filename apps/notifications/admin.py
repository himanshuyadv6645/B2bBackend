from django.contrib import admin
from .models import Notification, NotificationTemplate, DeviceToken


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read')


@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_type', 'is_active')
    list_filter = ('template_type', 'is_active')


@admin.register(DeviceToken)
class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'is_active', 'last_used_at', 'created_at')
    list_filter = ('platform', 'is_active')
    search_fields = ('user__email', 'token')
