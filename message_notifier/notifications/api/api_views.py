from rest_framework import generics
from notifications.api.serializers import NotificationSerializer
from notifications.models import Notification
from notifications.tasks import process_notification


class NotificationCreateView(generics.CreateAPIView):
    """
    API view для создания уведомлений.

    Этот класс наследует `CreateAPIView` из Django REST Framework и
    позволяет создавать объекты модели `Notification` через POST-запрос.

    Атрибуты:
        queryset (QuerySet): Набор всех уведомлений (`Notification.objects.all()`).
        serializer_class (Serializer): Сериализатор `NotificationSerializer` для валидации и сериализации данных.

    Методы:
        perform_create(serializer):
            Сохраняет новый объект уведомления и запускает асинхронную обработку
            через Celery задачу `process_notification`.

        create(request, *args, **kwargs):
            Переопределяет стандартный метод `create` для возврата сериализованных данных
            только что созданного уведомления, гарантируя актуальность данных после сохранения.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        notification = serializer.save()

        process_notification.delay(notification.id)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        notification = Notification.objects.get(id=response.data["id"])
        response.data = NotificationSerializer(notification).data
        return response


class NotificationDetailView(generics.RetrieveAPIView):
    """
    API view для получения детальной информации об уведомлении.

    Этот класс наследует `RetrieveAPIView` из Django REST Framework и
    позволяет получать данные конкретного уведомления по его ID. Смысл данного
    класса в просмотре информации после успешной отправки уведомлений - то есть,
    детализация времени отправки и канала. Это нужно потому, что в базовом эндпоинте
    мы не можем увидеть подобную информацию вследствие выполнения задачи в Celery -
    поэтому там данные поля заполняются null-значениями.

    Атрибуты:
        queryset (QuerySet): Набор всех уведомлений (`Notification.objects.all()`).
        serializer_class (Serializer): Сериализатор `NotificationSerializer` для сериализации данных.

    Методы:
        В стандартной реализации используется метод `retrieve`, предоставляемый `RetrieveAPIView`,
        который возвращает сериализованные данные уведомления по переданному ID.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer