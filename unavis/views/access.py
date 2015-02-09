from braces import views as braces_views
from django.core.urlresolvers import reverse_lazy


class DefaultLoginRequiredMixin(braces_views.LoginRequiredMixin):
    login_url = reverse_lazy('home')


class DefaultPermissionRequiredMixin(braces_views.PermissionRequiredMixin):
    login_url = reverse_lazy('home')
