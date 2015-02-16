import logging

from django.views import generic as generic_views

logger = logging.getLogger('django.views')


class HomeView(generic_views.TemplateView):
    template_name = 'core/home.html'

    def get(self, *args, **kwargs):
        logger.info('hitting home view')
        return super(HomeView, self).get(*args, **kwargs)
