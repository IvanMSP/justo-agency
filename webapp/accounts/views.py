# Django Core
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import login, logout


class LoginView(View):
    """
    View for login with email-pass.
    """

    def get(self, request):
        template_name = "accounts/login.html"
        return render(request, template_name)


class RegisterView(View):
    """
    View for register hitman with email-password
    """

    def get(self, request):
        template_name = "accounts/register.html"
        return render(request, template_name)


def logout_view(request):
    """
    Logout Function
    """
    logout(request)
    return redirect("login")
