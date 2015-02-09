from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput)
