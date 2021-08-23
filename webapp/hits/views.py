# Django Core
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

# Owner
from hits.models import Hit
from accounts.models import User, GroupHitman
from .forms import HitForm
from .utils.build_forms import get_hit_form


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
            hits = user.group_hitman.hits.all() | assignee
        else:
            hits = Hit.objects.all()
        return hits.order_by("-created")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HitDetailView(LoginRequiredMixin, View):
    template_name = "hits/hit-detail.html"

    def get(self, request, pk):
        user = request.user
        try:
            instance = get_object_or_404(Hit, pk=pk)
            form = get_hit_form(user, instance)
            context = {
                "instance": instance,
                "form": form if form is not None else "",
            }
            return render(request, self.template_name, context)
        except Hit.DoesNotExist:
            messages.error(
                request,
                "¡Hit no encontrado!",
            )
            return redirect("hits")

    def post(self, request, pk):
        user = request.user
        try:
            data = request.POST
            instance = get_object_or_404(Hit, pk=pk)
            if user.is_boss or user.is_manager:
                instance.assignee = User.objects.get(pk=int(data["assignee"]))
            elif user.is_hitman:
                instance.status = data["status"]
            instance.save()
            messages.success(
                request,
                "¡Hit actualizado correctamente!",
            )
            return redirect("hits")
        except Exception as e:
            messages.info(request, f"{e}")
            return redirect("hits")
