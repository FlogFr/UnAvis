"""
WSGI config for UnAvis project.

It exposes the WSGI callable as a module-level variable named application.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

DEBUG = os.getenv('DEBUG', False)
TEST = os.getenv('TEST', False)

if DEBUG:
    os.environ.setdefault("DJANGO_CONFIGURATION",
                          "DevelopmentConfiguration")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "UnAvis.settings.development")
elif TEST:
    os.environ.setdefault("DJANGO_CONFIGURATION",
                          "DefaultConfiguration")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "UnAvis.settings.defaults")
else:
    os.environ.setdefault("DJANGO_CONFIGURATION",
                          "ProductionConfiguration")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "UnAvis.settings.production")
from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
