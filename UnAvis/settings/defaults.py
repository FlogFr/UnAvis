"""
defaults settings
"""

import os
from yaml import load

from configurations import Configuration
from django.contrib.messages import constants as messages
from django.core.files import File


class DefaultConfiguration(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    DEFAULT_FROM_EMAIL = 'contact@1avis.fr'

    TEMPLATE_DEBUG = False

    ALLOWED_HOSTS = []

    SITE_ID = 1
    SITE_NAME = '1avis.fr'

    ADMINS = (
        ('Admin', 'contact@1avis.fr'),
        ('aRkadeFR', 'contact@arkade.info'),
    )

    # Application definition
    INSTALLED_APPS = (
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'django.contrib.flatpages',
        'UnAvis',
        'bootstrap3',
        'waffle',
        'mptt',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'UnAvis.middleware.MaintenanceModeMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
        "UnAvis.context_processors.menu",
    )

    MAINTENANCE_IGNORE_URLS = (
        r'^/login/.*',
        r'^/admin/.*'
        )

    ROOT_URLCONF = 'UnAvis.urls'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    LOGIN_REDIRECT_URL = '/'

    TEMPLATE_DIRS = (
        os.getcwd()+'/data/templates',
    )

    WSGI_APPLICATION = 'UnAvis.wsgi.application'

    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = False
    USE_L10N = False
    USE_TZ = True

    # DEBUG, INFO, WARNING, ERROR, CRITICAL
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
    }

    MESSAGE_TAGS = {
        messages.DEBUG: 'success',
        messages.INFO: 'info',
        messages.SUCCESS: 'success',
        messages.WARNING: 'warning',
        messages.ERROR: 'danger',
    }

    MEDIA_ROOT = os.getcwd()+'/data/uploads'

    # SECURITY WARNING: keep the secret key used in production secret!
    with open('data/settings/secret_key') as f:
        secret_key_file = File(f)
        SECRET_KEY = secret_key_file.read()

    # email settings
    with open('data/settings/email.yaml') as f:
        email_file = File(f)
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAILS = load(email_file)
        EMAIL_HOST = EMAILS['SERVER']
        EMAIL_PORT = EMAILS['PORT']
        EMAIL_HOST_USER = EMAILS['USER']
        EMAIL_HOST_PASSWORD = EMAILS['PASSWORD']
        EMAIL_USE_SSL = EMAILS['SSL']
        EMAIL_USE_TLS = EMAILS['TLS']
        EMAIL_FILE_PATH = '/tmp/emails'

    # DB settings
    with open('data/settings/database.yaml') as f:
        database_file = File(f)
        DATABASES = load(database_file)

    # active queue settings
    with open('data/settings/active_queue.yaml') as f:
        active_queue_file = File(f)
        ACTIVE_QUEUE = load(active_queue_file)
        BROKER_URL = ACTIVE_QUEUE['BROKER_URL']

    AUTH_USER_MODEL = 'UnAvis.User'
