from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    active = models.BooleanField('active status', default=False)
