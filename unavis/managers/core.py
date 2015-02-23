from django.contrib.auth.models import UserManager


class UserModelManager(UserManager):
    @property
    def ROBOT(self):
        return self.get_queryset().get(username='robot')


class UserModelValidatedManager(UserModelManager):
    def get_queryset(self):
        return super(UserModelValidatedManager, self).get_queryset(
        ).filter(
            validated_at__isnull=False,
        )
