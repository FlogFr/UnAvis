import logging

from django.views import generic as generic_views

logger = logging.getLogger('django.views')


class HomeView(generic_views.TemplateView):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)
