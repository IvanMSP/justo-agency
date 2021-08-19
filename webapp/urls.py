# Django
from django.urls import path
from django.urls.conf import include

# Owner
from .accounts.urls import urlpatterns as accounts_urls


urlpatterns = [
    path("", include(accounts_urls)),
]
