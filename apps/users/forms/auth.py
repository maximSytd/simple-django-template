from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomLoginForm(AuthenticationForm):
    """Custom login from."""

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Input username"),
            }
        ),
        label=_("Username"),
        required=False,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
            "class": "form-control",
            "placeholder": _("Input password"),
            }
        ),
        label=_("Password"),
        required=False,
    )
