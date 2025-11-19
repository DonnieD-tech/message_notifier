import os
import requests
from notifications.senders.base import BaseSender


class SMSSender(BaseSender):
    """
    Отправитель SMS через сервис SMS.ru.

    Наследуется от BaseSender и реализует метод send для отправки
    текстовых сообщений пользователям через API SMS.ru.

    Требования:
        - В файле .env должна быть переменная SMS_RU_API_ID с вашим api_id
          (находится в личном кабинете сервиса SMS.ru после регистрации)
        - Требуется зарегистрированный буквенный отправитель на SMS.ru.
          Вследствие того, что я не регистирировал его (это долго, т.к.
          требуется согласование операторов связи), фактическое получение смс
          не тестировалось, однако API SMS.ru используется строго по инструкции
          и работает верно, то есть при наличии буквенного отправителя работает.

    Методы:
        send(user, message):
            Отправляет SMS указанному пользователю.

            Аргументы:
                user: Объект пользователя с атрибутом `phone_number`.
                message (str): Текст сообщения.

            Возвращает:
                bool: True, если все SMS успешно отправлены, иначе False.

            Исключения:
                Все ошибки при отправке SMS обрабатываются внутри метода.
                При возникновении исключения выводится сообщение об ошибке и возвращается False.
    """

    def send(self, user, message):
        try:
            response = requests.get(
                "https://sms.ru/sms/send",
                params={
                    "api_id": os.getenv("SMS_RU_API_ID"),
                    "to": user.phone_number,
                    "msg": message,
                    "json": 1
                },
                timeout=10
            )
            result = response.json()
            sms_status = result.get("sms", {})
            success = True

            for number, info in sms_status.items():
                if info.get("status_code") == 100:
                    print(f"SMS успешно отправлено на {number}")
                else:
                    success = False
                    print(f"Ошибка SMS на {number}:"
                          f" {info.get('status_text')}"
                          f" (код {info.get('status_code')})")

            return success

        except Exception as e:
            print(f"Ошибка при отправке через SMS: {e}")
            return False



