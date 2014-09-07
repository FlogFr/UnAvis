from braces import views as braces_views
from django.core.urlresolvers import reverse_lazy


class DefaultLoginRequiredMixin(braces_views.LoginRequiredMixin):
    """
    View mixin which verifies that the user is authenticated.

    NOTE:
        This should be the left-most mixin of a view, except when
        combined with CsrfExemptMixin - which in that case should
        be the left-most mixin.
    """
    def get_login_url(self):
        return reverse_lazy('home')


class DefaultPermissionRequiredMixin(braces_views.PermissionRequiredMixin):
    """
    View mixin which verifies that the logged in user has the specified
    permission.

    Class Settings
    `permission_required` - the permission to check for.
    `redirect_field_name` - defaults to "next"
    `raise_exception` - defaults to False - raise 403 if set to True

    Example Usage

        class SomeView(PermissionRequiredMixin, ListView):
            ...
            # required
            permission_required = "app.permission"

            # optional
            redirect_field_name = "hollaback"
            raise_exception = True
            ...
    """
    def get_login_url(self):
        return reverse_lazy('home')
