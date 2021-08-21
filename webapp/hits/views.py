# Django Core
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

# Owner
from hits.models import Hit
from .forms import HitForm


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


class HitDetailView(LoginRequiredMixin, View):
    template_name = "hits/hit-detail.html"

    def get(self, request, pk):
        instance = get_object_or_404(Hit, pk=pk)
        form = HitForm(instance=instance)
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)
