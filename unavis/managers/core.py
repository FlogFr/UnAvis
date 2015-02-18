from django.contrib.auth.models import UserManager


class UserModelManager(UserManager):
    @property
    def ROBOT(self):
        return self.get_queryset().get(username='robot')
