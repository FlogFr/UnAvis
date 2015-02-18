import logging

from django.views import generic as generic_views
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from unavis import models
from unavis import forms

logger = logging.getLogger('django.forms')


class CategoryList(generic_views.ListView):
    model = models.Category


class CategoryCreate(generic_views.CreateView):
    model = models.Category
    form_class = forms.CategoryForm

    def form_valid(self, form):
        form.save(self.request)
        return HttpResponseRedirect(reverse('home'))
