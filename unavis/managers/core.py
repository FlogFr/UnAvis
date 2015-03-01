from django.contrib.auth.models import UserManager
from django.db import models


class UserModelQuerySet(models.query.QuerySet):
    pass


class UserModelManager(UserManager):
    pass
