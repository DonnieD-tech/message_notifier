from rest_framework import generics
from users.api.serializers import UserCreateSerializer
from users.models import User


class UserCreateAPIView(generics.CreateAPIView):
    """
    API view для создания нового пользователя.

    Наследуется от `CreateAPIView` Django REST Framework и
    позволяет регистрировать пользователей через POST-запрос.

    Атрибуты:
        queryset (QuerySet): Набор всех пользователей (`User.objects.all()`).
        serializer_class (Serializer): Сериализатор `UserCreateSerializer` для валидации и создания пользователей.

    Методы:
        В стандартной реализации используется метод `create`, предоставляемый `CreateAPIView`,
        который создает пользователя и возвращает сериализованные данные.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
