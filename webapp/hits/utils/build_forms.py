# DJANGO CORE IMPORTS
from django import forms
from django.db.models import Q

# Owner
from reusable.choices import StatusType
from hits.models import Hit
from accounts.models import User

status_closed_hit = [2, 3]


def get_hit_form(user, instance):
    """
    Return HitForm Class
    """
    if user.is_hitman and instance.status not in StatusType.choices_hitman():
        fields = {
            "status": forms.ChoiceField(
                choices=StatusType.choices_hitman(),
                widget=forms.Select(attrs={"class": "form-control pl-5"}),
            )
        }
        return type("HitForm", (forms.BaseForm,), {"base_fields": fields})
    elif user.is_boss and instance.status not in StatusType.choices_hitman():
        fields = {
            "assignee": forms.ModelChoiceField(
                queryset=User.objects.filter(
                    Q(is_hitman=True) | Q(is_manager=True)
                ).exclude(pk=user.pk),
                widget=forms.Select(attrs={"class": "form-control pl-5"}),
            )
        }
        return type("HitForm", (forms.BaseForm,), {"base_fields": fields})
    elif user.is_manager and instance.status not in StatusType.choices_hitman():
        fields = {
            "assignee": forms.ModelChoiceField(
                queryset=user.group_hitman.hitmans.all()
                .exclude(user__status=False)
                .exclude(pk=user.pk),
                widget=forms.Select(attrs={"class": "form-control pl-5"}),
            )
        }
        return type("HitForm", (forms.BaseForm,), {"base_fields": fields})
