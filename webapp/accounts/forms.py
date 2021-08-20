# Django Core
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

# Owner
from accounts.models import User


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control pl-5", "placeholder": "Nombre"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control pl-5", "placeholder": "Apellidos"}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control pl-5", "placeholder": "Email"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control pl-5", "placeholder": "Contraseña"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control pl-5", "placeholder": "Repite contraseña"}
        )
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password", "password2")

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            self.add_error("password2", "Las contraseñas no coinciden")


class LoginForm(forms.Form):
    """LoginForm definition."""

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control pl-5",
                "placeholder": "Email",
                "name": "email",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control pl-5",
                "placeholder": "Contraseña",
                "name": "password",
            }
        )
    )
