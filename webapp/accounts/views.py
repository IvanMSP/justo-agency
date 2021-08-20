# Django Core
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Owner
from .forms import RegisterForm, LoginForm
from accounts.models import User, ProfileHitman, GroupHitman


class LoginView(View):
    """
    View for login with email-pass.
    """

    template_name = "accounts/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("hits")
        form = LoginForm()
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user = authenticate(
                username=loginForm.cleaned_data["email"],
                password=loginForm.cleaned_data["password"],
            )
            if user is None:
                messages.error(
                    request,
                    "Tú email ó contraseña son incorrectos, ¡Vuelve a intentar!",
                )
                return redirect("login")
            messages.success(
                request,
                "¡Acceso exitoso!",
            )
            login(request, user)
            return redirect("hits")
        else:
            if loginForm.errors:
                for field in loginForm:
                    for error in field.errors:
                        messages.info(request, error)
            context = {"form": loginForm}
            return render(request, self.template_name, context)


class RegisterView(View):
    """
    View for register hitman with email-password
    """

    template_name = "accounts/register.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("hits")
        form = RegisterForm()
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create(
                first_name=cd["first_name"],
                last_name=cd["last_name"],
                email=cd["email"],
                is_hitman=True,
            )
            user.set_password(cd["password"])
            user.save()
            profile = ProfileHitman.objects.create_profile(user)
            profile.group_hitman = GroupHitman.objects.get(pk=1)
            profile.save()
            login(request, user)
            return redirect("hits")
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.info(request, error)
            context = {"form": RegisterForm()}
            return render(request, self.template_name, context)


def logout_view(request):
    """
    Logout Function
    """
    messages.success(
        request,
        "¡Hasta pronto!",
    )
    logout(request)
    return redirect("login")
