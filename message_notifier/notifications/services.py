from django.utils import timezone

from .constants import CHANNEL_ORDER, MAX_RETRIES
from .senders.sms import SMSSender
from .senders.email import EmailSender
from .senders.telegram import TelegramSender

SENDERS_MAP = {
    "email": EmailSender(),
    "sms": SMSSender(),
    "telegram": TelegramSender(),
}


class NotificationService:
    @staticmethod
    def send_notification(notification):
        """
        Пытается отправить уведомление синхронно с fallback по каналам.
        Выполняет ретраи при полном провале.
        """

        user = notification.user
        message = notification.message

        if notification.retry_count >= MAX_RETRIES:
            notification.status = "failed"
            notification.save(update_fields=["status"])
            return notification

        for channel in CHANNEL_ORDER:
            sender = SENDERS_MAP[channel]

            try:
                success = sender.send(user, message)
            except Exception as e:
                success = False

            notification.last_channel = channel

            if success:
                notification.status = "sent"
                notification.sent_at = timezone.now()
                notification.save(update_fields=["status", "last_channel", "sent_at"])
                return notification

        notification.retry_count += 1
        notification.save(update_fields=["retry_count", "last_channel"])

        return notification
