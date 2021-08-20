# Django Core
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import login, logout


class HitsView(LoginRequiredMixin, View):
    """
    View list for Hits
    """

    def get(self, request):
        template_name = "hits/list_hits.html"
        return render(request, template_name)
