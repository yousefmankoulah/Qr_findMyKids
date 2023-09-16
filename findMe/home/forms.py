from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, label=_("Email"))

    class Meta:
        model = User
        fields = (_('first_name'), 'last_name', 'email', 'username', 'password1', 'password2')