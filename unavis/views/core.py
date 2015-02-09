from django.views import generic as generic_views
from unavis import models

class CategoryCreate(generic_views.CreateView):
    model = models.Category
