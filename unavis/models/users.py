from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.utils import timezone
from unavis import managers


class UserModel(AbstractBaseUser, PermissionsMixin):
    """
    ```UserModel``` defines all the user on the
    website. It can be either anonymous, the admin
    or anyone else. It abstracts and stay very close
    the the django.contrib.auth packages models to
    work with for permissions and groups.
    """
    email = models.EmailField(_('email address'),
                              primary_key=True, unique=True,
                              null=False, blank=False)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether '
                                               'the user can log into '
                                               'this admin site.'))
    validated_at = models.DateTimeField(_('DateTime an account is validated'),
                                        null=True, default=None,
                                        editable=False)
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether the active'
                                                ' flag of the user. '))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = managers.UserModelManager.from_queryset(
        managers.UserModelQuerySet
    )()

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        abstract = False

    @property
    def validated(self):
        return bool(self.validated_at is not None)
