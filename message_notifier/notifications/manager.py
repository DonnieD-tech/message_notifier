class NotificationManager:
    """
    Менеджер уведомлений, отвечающий за отправку сообщений через несколько каналов.

    Этот класс принимает список объектов отправителей (Sender) и позволяет
    отправлять одно и то же сообщение пользователю через все заданные каналы.

    Атрибуты:
        senders (list[BaseSender]): Список объектов отправителей, которые реализуют метод send(user, message).

    Методы:
        notify(user, message):
            Отправляет сообщение пользователю через все доступные каналы.

            Аргументы:
                user: Объект пользователя, содержащий контактные данные (email, phone_number и т.д.).
                message (str): Текст уведомления.

            Возвращает:
                dict: Результаты отправки для каждого канала в формате:
                    {
                        "EmailSender": "OK" / "FAIL" / "ERROR: <текст ошибки>",
                        "SMSSender": "OK" / "FAIL" / "ERROR: <текст ошибки>",
                        ...
                    }

            Особенности:
                - Исключения при отправке конкретным каналом обрабатываются внутри метода,
                  чтобы не прерывать отправку через другие каналы.
                - Каналы обрабатываются в том порядке, в котором они переданы в конструктор.
    """
    def __init__(self, senders):
        self.senders = senders

    def notify(self, user, message: str) -> dict:
        results = {}
        for sender in self.senders:
            sender_name = sender.__class__.__name__
            try:
                success = sender.send(user, message)
                results[sender_name] = "OK" if success else "FAIL"
            except Exception as e:
                results[sender_name] = f"ERROR: {e}"
        return results
