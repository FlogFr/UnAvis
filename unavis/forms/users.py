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

    def clean_email(self):
        email = self.cleaned_data['email']
        UserModel = get_user_model()
        if UserModel.objects.filter(email=email).exists():
            return email
        elif UserModel.objects_all.filter(email=email).exists():
            raise forms.ValidationError(
                _('This email is on waiting validation'),
                code='login_email_waiting_validation',
            )
        else:
            raise forms.ValidationError(
                _('This email doesnt belong to an account'),
                code='login_email_not_exist',
            )

    def clean(self):
        email = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)

        if email and password:
            self.user_session = authenticate(email=email,
                                             password=password)
            if self.user_session is None:
                raise forms.ValidationError(
                    _('Password provided doesnt match the account'),
                    code='login_invalid_password',
                )

        return self.cleaned_data


class SignUpForm(SecureBotForm):
    email = forms.EmailField(label=_('Email address'), required=True)
    password = forms.CharField(label=_('Password'), required=True,
                               widget=forms.PasswordInput)
    first_name = forms.CharField(label=_('First Name'), required=False)
    last_name = forms.CharField(label=_('Last Name'), required=False)

    def clean_email(self):
        # if an email is already taken & validated
        UserModel = get_user_model()
        email = self.cleaned_data['email']
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError(
                _('Email already taken'),
                code='signup_email_already_taken',
            )
        elif UserModel.objects_all.filter(email=email).exists():
            raise forms.ValidationError(
                _('Email on waiting validation'),
                code='signup_email_waiting_validation',
            )

        return email

    def save(self):
        UserModel = get_user_model()

        email = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)
        first_name = self.cleaned_data.get('first_name', None)
        last_name = self.cleaned_data.get('last_name', None)

        self.user = UserModel(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=False,
            validated_at=None,
        )
        self.user.set_password(password)
        self.user.save()

        self.user_session = authenticate(email=email,
                                         password=password)
        if self.user_session is None:
            raise forms.ValidationError(
                _('Password provided doesnt match the account'),
                code='login_invalid_password',
            )

        return self.user_session

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
