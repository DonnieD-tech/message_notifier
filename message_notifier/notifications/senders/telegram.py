import requests
import os
from notifications.senders.base import BaseSender


class TelegramSender(BaseSender):
    """
    Отправитель сообщений через Telegram.

    Наследуется от BaseSender и реализует метод send для отправки
    уведомлений пользователям через Telegram Bot API.

    Требования:
        - В файле .env должны быть переменные:
            - TELEGRAM_BOT_TOKEN: токен вашего бота (создается через BotFather)
            - TELEGRAM_CHAT_ID: ID чата, куда отправлять сообщения.


    Методы:
        send(user, message):
            Отправляет сообщение пользователю через Telegram.

            Аргументы:
                user: объект пользователя (не используется напрямую,
                      чат берется из .env).
                message (str): текст сообщения.

            Возвращает:
                bool: True, если сообщение успешно отправлено (HTTP 200), иначе False.

            Исключения:
                Все ошибки при отправке сообщения обрабатываются внутри метода.
                При возникновении исключения выводится сообщение об ошибке и возвращается False.
    """
    def send(self, user, message):
        try:
            url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
            payload = {
                "chat_id": os.getenv('TELEGRAM_CHAT_ID'),
                "text": message
            }
            r = requests.post(url, json=payload)
            return r.status_code == 200

        except Exception as e:
            print(f"Ошибка отправки через Телеграмм: {e}")
            return False


