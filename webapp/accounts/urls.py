# Django
from django.urls import path
from django.urls.conf import include

# Owner
from webapp.accounts.views import LoginView, RegisterView


urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
]
