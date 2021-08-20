# Django Core
from webapp.accounts.views import logout_view
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView
from django.contrib.auth import login, logout

# Owner
from hits.models import Hit


class HitsView(LoginRequiredMixin, ListView):
    """
    View list for Hits
    """

    model = Hit
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        if user.is_hitman:
            hits = user.assignee.all()
        elif user.is_manager:
            assignee = user.assignee.all()
            assignee_by = user.assignee_by.all()
            hits = assignee | assignee_by
        else:
            hits = Hit.objects.all()
        return hits.order_by("-created")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
