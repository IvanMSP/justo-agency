# Django Core
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# Owner
from webapp.urls import urlpatterns as webapp_urls


urlpatterns = [
    path("agency-hitmen/", admin.site.urls),
    path("webapp/", include(webapp_urls)),
]
