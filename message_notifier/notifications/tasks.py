from celery import shared_task
from .models import Notification
from .services import NotificationService


@shared_task
def process_notification(notification_id):
    notification = Notification.objects.get(pk=notification_id)

    result = NotificationService.send_notification(notification)

    return {"status": "ok", "id": notification.id}
