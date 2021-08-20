# Django
from django.urls import path
from django.urls.conf import include

# Owner
from .views import HitsView


urlpatterns = [
    path("hits", HitsView.as_view(), name="hits"),
]
