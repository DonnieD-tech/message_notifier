import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "message_notifier.settings")

app = Celery("message_notifier")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
