from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class User(AbstractUser):
    """
    Кастомная модель пользователя, основанная на Django `AbstractUser`.

    Использует email в качестве поля для аутентификации вместо username.
    Добавляет дополнительные поля для работы с контактными данными пользователя.

    Атрибуты:
        email (EmailField): Уникальный адрес электронной почты пользователя, используется как идентификатор.
        phone_number (CharField): Номер телефона пользователя.
        telegram_id (CharField): ID пользователя в Telegram (необязательное поле).

        USERNAME_FIELD (str): Поле, используемое для аутентификации (email).
        REQUIRED_FIELDS (tuple): Поля, обязательные при создании пользователя через createsuperuser.

        objects (UserManager): Менеджер пользователей, реализующий методы create_user и create_superuser.

    Методы:
        __str__():
            Возвращает строковое представление пользователя — его email.
    """
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    telegram_id = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'first_name',
        'last_name'
    )

    objects = UserManager()

    def __str__(self):
        return self.email

