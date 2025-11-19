from django.urls import path
from notifications.api.api_views import NotificationCreateView, NotificationDetailView


urlpatterns = [
    path("create/", NotificationCreateView.as_view(), name="notifications-create"),
    path('<int:pk>/', NotificationDetailView.as_view(), name="notifications-detail"),
]
