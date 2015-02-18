from django.db.models import manager
from mptt import managers as mptt_managers


class CommonManager(manager.Manager):
    pass


class TreeManager(mptt_managers.TreeManager):
    pass
