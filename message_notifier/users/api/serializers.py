from rest_framework import serializers
from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания нового пользователя.

    Отвечает за валидацию данных при регистрации пользователя и
    корректное сохранение пароля (с хешированием).

    Атрибуты Meta:
        model (Model): Модель User, с которой работает сериализатор.
        fields (list): Поля модели, которые будут доступны для создания пользователя:
            - email
            - password
            - first_name
            - last_name
            - telegram_id
            - phone_number
        extra_kwargs (dict): Дополнительные аргументы для полей:
            - password: только для записи (write_only), не будет возвращаться в ответах API.

    Методы:
        create(validated_data):
            Создает пользователя с хешированным паролем.

            Аргументы:
                validated_data (dict): Валидированные данные для создания пользователя.

            Возвращает:
                User: Объект только что созданного пользователя.
    """
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "telegram_id",
            "phone_number"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
