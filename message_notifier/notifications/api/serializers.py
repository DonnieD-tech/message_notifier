from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Notification.

    Отвечает за валидацию и преобразование данных уведомлений
    для API-запросов и ответов.

    Атрибуты Meta:
        model (Model): Модель Notification, с которой работает сериализатор.
        fields (tuple): Поля модели, которые будут сериализованы:
            - id: уникальный идентификатор уведомления
            - user: пользователь, которому адресовано уведомление
            - message: текст уведомления
            - status: текущий статус уведомления (например, 'sent', 'pending')
            - retry_count: количество попыток отправки уведомления
            - last_channel: последний использованный канал отправки
            - sent_at: дата и время последней отправки
            - created_at: дата и время создания уведомления
        read_only_fields (tuple): Поля только для чтения, которые нельзя изменять через API:
            - status
            - retry_count
            - last_channel
            - sent_at
            - created_at
    """
    class Meta:
        model = Notification
        fields = (
            "id",
            "user",
            "message",
            "status",
            "retry_count",
            "last_channel",
            "sent_at",
            "created_at",
        )
        read_only_fields = (
            "status",
            "retry_count",
            "last_channel",
            "sent_at",
            "created_at"
        )