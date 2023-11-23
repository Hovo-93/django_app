"""
Файл настроек Celery
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import
import os
from celery import Celery
import django
from django.conf import settings

# этот код скопирован с manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')
django.setup()

# здесь вы меняете имя
app = Celery("django_app")

# Для получения настроек Django, связываем префикс "CELERY" с настройкой celery
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'
# загрузка tasks.py в приложение django
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('request.'.format(self.request))