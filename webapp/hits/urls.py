# Django
from django.urls import path
from django.urls.conf import include

# Owner
from .views import HitsView, HitDetailView, CreateHitView


urlpatterns = [
    path("hits", HitsView.as_view(), name="hits"),
    path("hits/create", CreateHitView.as_view(), name="hit-create"),
    path("hits/<int:pk>", HitDetailView.as_view(), name="hit-detail"),
]
