from django.conf import settings
from django.db import models

class Notification(models.Model):
    """
    Модель уведомления пользователя.

    Сохраняет информацию о сообщениях, отправляемых пользователям,
    включая текст уведомления, статус отправки, количество попыток и канал.

    Атрибуты:
        STATUS_CHOICES (tuple): Варианты статуса уведомления:
            - "pending": уведомление ожидает отправки
            - "sent": уведомление успешно отправлено
            - "failed": отправка уведомления завершилась неудачей

        CHANNEL_CHOICES (tuple): Варианты канала отправки:
            - "sms": SMS
            - "email": Email
            - "telegram": Telegram

        user (ForeignKey): Пользователь, которому адресовано уведомление.
        message (TextField): Текст уведомления.
        status (CharField): Статус уведомления, по умолчанию "pending".
        retry_count (IntegerField): Количество попыток отправки уведомления.
        last_channel (CharField): Последний использованный канал отправки.
        sent_at (DateTimeField): Дата и время последней отправки.
        created_at (DateTimeField): Дата и время создания уведомления.

    Методы:
        __str__():
            Возвращает строковое представление уведомления в формате:
            'Notification <id> to <user>'.
    """
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("sent", "Sent"),
        ("failed", "Failed"),
    )

    CHANNEL_CHOICES = (
        ("sms", "SMS"),
        ("email", "Email"),
        ("telegram", "Telegram"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    message = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending"
    )
    retry_count = models.IntegerField(
        default=0
    )
    last_channel = models.CharField(
        max_length=10,
        choices=CHANNEL_CHOICES,
        null=True,
        blank=True
    )
    sent_at = models.DateTimeField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Notification {self.pk} to {self.user}'
