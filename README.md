# Notification Service

Сервис для отправки уведомлений пользователям через несколько каналов: Email, SMS и Telegram.  
Подходит для интеграции с другими проектами на Django.
Является реализацией тестового задания для компании Photo Point.

---

## Основные возможности

- Создание уведомлений через API.
- Поддержка нескольких каналов доставки:
  - Email (SMTP)
  - SMS (через SMS.ru)
  - Telegram (через Bot API)
- Асинхронная обработка уведомлений через Celery.
- Логирование и возврат статуса отправки по каждому каналу.
- Повторные попытки отправки при ошибках (настраиваемое количество и задержка).

---

## Установка и настройка

1. Клонируйте репозиторий:
   git clone <URL_репозитория>
   cd notification_service

   
2. Создайте .env файл в корне проекта:
    # Django
    DEBUG=True
    SECRET_KEY=<ваш секретный ключ>
    
    # Database
    POSTGRES_DB=<имя для базы>
    POSTGRES_USER=<пользователь>
    POSTGRES_PASSWORD=<пароль>
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    
    # Email
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_PORT=465
    EMAIL_HOST_USER=<адрес почты gnail, куда будем принимать уведомления>
    EMAIL_HOST_PASSWORD=<тут необходим app password, который можно создать через гугл аккаунт>
    EMAIL_USE_TLS=False
    EMAIL_USE_SSL=True
    
    # Telegram
    TELEGRAM_BOT_TOKEN=<токен бота, который будет заниматься отправкой>
    TELEGRAM_CHAT_ID=<id чата юзера, куда будут приходить сообщения от бота>
    
    # SMS.ru
    SMS_SENDER_NAME=Notifier
    SMS_RU_API_ID=<id из личного кабинета SMS.ru>

3. Постройте Docker-образ и запустите контейнеры:
    docker-compose up --build

Далее интерфейс сервиса доступен в виде API-документации по адресу:
http://localhost:8000/

API

Создание пользователя
    Endpoint: POST /api/users/
    Поля: email, password, first_name, last_name, telegram_id, phone_number
    Пример ответа:

Создание уведомления
    Endpoint: POST /api/notifications/
    Автоматически запускается Celery задача process_notification.
    Пример ответа:

Получение уведомления
    Endpoint: GET /api/notifications/<id>/
    Возвращает детальную информацию о уведомлении.
    Пример ответа:


Конфигурация отправителей

Список доступных отправителей:
    EmailSender – отправка через SMTP.
    SMSSender – отправка через SMS.ru.
    TelegramSender – отправка через Telegram Bot API.

Порядок отправки можно настроить через константу CHANNEL_ORDER:
    CHANNEL_ORDER = ("sms", "email", "telegram")

Максимальное количество попыток и задержка между ними:
    MAX_RETRIES = 3
    RETRY_DELAY_SECONDS = 60


Технологии
    Python 3.12
    Django 5.x
    Django REST Framework
    Celery + Redis (асинхронная обработка уведомлений)
    PostgreSQL
    Docker + Docker Compose
    requests (для SMS и Telegram API)
    smtplib (отправка Email через SMTP)

