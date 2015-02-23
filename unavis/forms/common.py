from django import forms
from django.utils.translation import ugettext_lazy as _

import logging

logger = logging.getLogger('django.forms')


def secure_bot_validator(data):
    if data is not False:
        raise forms.ValidationError(
            _('Bot not allowed'),
            code='form_secure_bot_warning',
        )


class SecureBotForm(forms.Form):
    bot_secured = forms.BooleanField(required=False,
                                     widget=forms.HiddenInput(),
                                     validators=[secure_bot_validator])
