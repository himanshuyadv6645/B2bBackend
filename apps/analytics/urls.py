from django.urls import path
from apps.analytics.views.analytics import (
    TrackEventView,
    EventStatsView,
    PopularEntitiesView,
)

app_name = 'analytics'

urlpatterns = [
    path('track/', TrackEventView.as_view(), name='track-event'),
    path('stats/', EventStatsView.as_view(), name='event-stats'),
    path('popular/', PopularEntitiesView.as_view(), name='popular-entities'),
]
