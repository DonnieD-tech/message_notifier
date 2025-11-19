import smtplib
import os
from email.mime.text import MIMEText
from notifications.senders.base import BaseSender


class EmailSender(BaseSender):
    """
    Отправитель сообщений по электронной почте.

    Наследуется от BaseSender и реализует метод send для отправки
    уведомлений пользователям через SMTP с использованием SSL.

    Методы:
        send(user, message):
            Отправляет email-сообщение указанному пользователю.

            Аргументы:
                user: Объект пользователя с атрибутом `email`.
                message (str): Текст сообщения.

            Возвращает:
                bool: True, если сообщение успешно отправлено, иначе False.

            Исключения:
                Все ошибки при отправке email обрабатываются внутри метода.
                При возникновении исключения выводится сообщение об ошибке и
                возвращается False.
    """
    def send(self, user, message):
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'Notification'
            msg['From'] = os.getenv('EMAIL_HOST_USER')
            msg['To'] = user.email

            with smtplib.SMTP_SSL(os.getenv('EMAIL_HOST'), int(os.getenv('EMAIL_PORT'))) as server:
                server.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
                server.send_message(msg)

            return True

        except Exception as e:
            print(f"Ошибка при отправке через Email: {e}")
            return False


