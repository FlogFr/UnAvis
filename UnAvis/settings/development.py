"""
Django development settings for 1Avis project.
"""

from UnAvis.settings.defaults import DefaultConfiguration

import os

import logging
logger = logging.getLogger(__name__)


class DevelopmentConfiguration(DefaultConfiguration):
    DEBUG = True
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    TEMPLATE_DEBUG = False
    TEMPLATE_DIRS = (os.getcwd()+'/data/templates',)

    ALLOWED_HOSTS = ['127.0.0.1',
                     'localhost']

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/
    STATIC_URL = '/static/'
    # where to copy the static file
    STATIC_ROOT = '/tmp/static'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        )

    INSTALLED_APPS = DefaultConfiguration.INSTALLED_APPS + (
        'django.contrib.admin',
        'debug_toolbar',
        'django_extensions',
        )

    MIDDLEWARE_CLASSES = DefaultConfiguration.MIDDLEWARE_CLASSES + (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        )

    DEV_LOGGING = {
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/tmp/1avis.log',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'UnAvis': {
                'handlers': ['console', 'file'],
                'propagate': True,
                'level': 'DEBUG',
            },
        },
        'formatters': {
            'verbose': {
                'format': '[%(asctime)s] [%(levelname)s] \
                [%(module)s] [%(process)d] [%(thread)d] %(message)s',
            },
        },
    }

    LOGGING = dict(list(DEV_LOGGING.items()) +
                   list(DefaultConfiguration.LOGGING.items()))
