from django.views import generic as generic_views
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import login
from django.contrib.auth.views import logout
from django.contrib import messages
from unavis import forms

import logging

logger = logging.getLogger('django.views')


class LoginView(generic_views.FormView):
    template_name = 'users/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.user_session)
        if not form.user_session.validated:
            messages.info(self.request, _('Please confirm your email,'
                                          'check your emails'))

        return super(LoginView, self).form_valid(form)


class LogoutView(generic_views.TemplateView):
    template_name = 'users/logout.html'

    def get(self, request, *args, **kwargs):
        return logout(self.request,
                      'home',
                      'users/logout.html',
                      self.request.GET.get('next', None), )


class RegenPasswordView(generic_views.FormView):
    template_name = 'users/regen_password.html'
    form_class = forms.RegenPasswordForm
    success_url = reverse_lazy('home')
