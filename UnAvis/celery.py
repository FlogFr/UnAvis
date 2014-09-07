from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
DEBUG = os.getenv('DEBUG', False)
TEST = os.getenv('TEST', False)

if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "UnAvis.settings.development")
elif TEST:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "UnAvis.settings.defaults")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "UnAvis.settings.production")

app = Celery('UnAvis',
             backend='amqp',
             include=['UnAvis.tasks'])

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()
