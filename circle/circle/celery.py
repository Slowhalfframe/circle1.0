from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'circle.settings')

app = Celery('users',
            broker='redis://192.168.0.104:6379/1',
            backend='redis://192.168.0.104:6379/2'
             )
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)