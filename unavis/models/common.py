from django.db import models
from django.conf import settings


class InvincibleModel(models.Model):
    """
    ```InvincibleModel``` enables the model to
    never be deleted from the DB by a .delete()
    """
    is_active = models.BooleanField('Is the object active',
                                    null=False, default=True, editable=False, )

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


class BaseModel(models.Model):
    """
    ```BaseModel``` gives a set of common fields as created_at
    """
    created_at = models.DateTimeField('Created time object',
                                      auto_now_add=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name='User who created the object',
                                   related_name='%(class)s_created',
                                   editable=False)
    updated_at = models.DateTimeField('Last time the object was updated',
                                      auto_now=True, editable=False)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name='Last user who updated object',
                                   related_name='%(class)s_updated',
                                   editable=False)

    class Meta:
        abstract = True


class ValidableModel(models.Model):
    """
    ```ValidableModel``` add a is_validated field
    """
    is_validated = models.BooleanField('Is validated',
                                       null=False, default=False, )

    class Meta:
        abstract = True


class TitleModel(models.Model):
    """
    ```TitleModel``` always contains a title and a
    description
    """
    title = models.CharField('Title',
                             max_length=1024,
                             null=True, default=None, )
    description = models.CharField('Description',
                                   max_length=20480,
                                   null=True, default=None, )

    class Meta:
        abstract = True


class SlugModel(models.Model):
    """
    ```SlugModel``` are public object that need a slug
    for the URL
    """
    slug = models.SlugField('Slug',
                            null=False, editable=False)

    class Meta:
        abstract = True
