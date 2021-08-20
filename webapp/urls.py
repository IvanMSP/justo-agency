# Django
from django.urls import path
from django.urls.conf import include

# Owner
from .accounts.urls import urlpatterns as accounts_urls
from .hits.urls import urlpatterns as hits_urls


urlpatterns = [
    path("", include(accounts_urls)),
    path("", include(hits_urls)),
]
