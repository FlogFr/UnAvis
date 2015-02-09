from django.db import models
from mptt import models as mptt_models
from unavis.models import common as common_models

from unavis import managers


class BaseCoreModel(common_models.InvincibleModel,
                    common_models.BaseModel):
    """
    Define a set of template model for
    all the core model
    """
    class Meta:
        abstract = True


class Category(BaseCoreModel,
               common_models.TitleModel,
               mptt_models.MPTTModel):
    """
    ```Category``` model defines a group of pages
    The user can sort the pages by category. An
    example of category is: France, Wine, Restaurant,
    Movies…
    """
    parent = mptt_models.TreeForeignKey('self',
                                        related_name='children',
                                        null=True, blank=True, )
                            

class Page(BaseCoreModel,
           common_models.TitleModel,
           common_models.SlugModel):
    """
    A ```Page``` is sorted in a ```Category``` and
    can be reviewed by ```UserModel```
    """
    category = models.ForeignKey(Category,
                                 editable=False,
                                 related_name='pages')


class Review(BaseCoreModel,
             common_models.TitleModel):
    """
    A ```review``` is set of notes, computing a global note
    and…
    """
    page = models.ForeignKey(Page,
                             null=False, )
    note = models.PositiveSmallIntegerField('Global note',
                                            null=False, default=0, )
