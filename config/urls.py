# Django Core
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# Owner
from webapp.urls import urlpatterns as webapp_urls
from webapp.accounts.views import handler_404_requests


urlpatterns = [
    path("agency/", admin.site.urls),
    path("webapp/", include(webapp_urls)),
]

handler404 = handler_404_requests
