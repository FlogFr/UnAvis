from django import forms
from unavis.forms import SecureBotForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

import logging

logger = logging.getLogger('django.forms')


class LoginForm(SecureBotForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)

        UserModel = get_user_model()

        if not self.errors:
            # we havent any field errors

            if UserModel.objects.filter(email=email).exists():
                # we are in a simple login
                logger.info('User {!s} logged in'.format(email))
                self.user_session = authenticate(email=email,
                                                 password=password)
                if self.user_session is None:
                    raise forms.ValidationError(
                        _('Password provided doesnt match the account'),
                        code='login_invalid_password',
                    )
            else:
                # we are signin
                user = UserModel.objects.create(email=email)
                user.set_password(password)
                user.save()
                logger.info('User signed-in: {!s}'.format(email))

                self.user_session = authenticate(email=email,
                                                 password=password)

        return self.cleaned_data


class RegenPasswordForm(SecureBotForm):
    email = forms.EmailField(label=_('Email address'), required=True)

    def clean_email(self):
        UserModel = get_user_model()
        email = self.cleaned_data['email']
        if not UserModel.objects_all.filter(email=email).exists():
            raise forms.ValidationError(
                _('This email doesnt exists'),
                code='regen_password_email_not_exists',
            )
