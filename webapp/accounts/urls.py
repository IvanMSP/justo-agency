# Django
from django.urls import path
from django.urls.conf import include

# Owner
from webapp.accounts.views import LoginView, RegisterView, logout_view


urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("logout", logout_view, name="logout"),
]
