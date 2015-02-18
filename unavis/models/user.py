from django.contrib.auth.models import AbstractUser
from unavis import managers


class UserModel(AbstractUser):
    """
    ```UserModel``` defines all the user on the
    website. It can be either anonymous, the admin
    or anyone else. It abstracts and stay very close
    the the django.contrib.auth packages models to
    work with for permissions and groups.
    """
    objects = managers.UserModelManager()
