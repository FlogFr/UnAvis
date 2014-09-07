"""
Defaults views
"""

from django.views.generic import (
    TemplateView,
    FormView,
)
from UnAvis import forms
from django.contrib import messages

import logging
logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = 'common/home.html'


class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = forms.SignUpForm
