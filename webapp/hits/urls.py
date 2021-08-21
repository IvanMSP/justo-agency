# Django
from django.urls import path
from django.urls.conf import include

# Owner
from .views import HitsView, HitDetailView


urlpatterns = [
    path("hits", HitsView.as_view(), name="hits"),
    path("hits/<int:pk>", HitDetailView.as_view(), name="hit-detail"),
]
