# DJANGO CORE IMPORTS
from django import forms
from django.db.models import Q

# Onwer
from hits.models import Hit
from accounts.models import User, GroupHitman
from reusable.choices import StatusType


class HitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(HitForm, self).__init__(*args, **kwargs)
        self.fields["assignee_by"].initial = user
        self.fields["status"].initial = StatusType.assigned.value
        if user.is_manager:
            self.fields["assignee"].queryset = user.group_hitman.hitmans.all().exclude(
                user__status=False
            )
        else:
            self.fields["assignee"].queryset = (
                User.objects.all().exclude(status=False).exclude(is_staff=True)
            )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control pl-5", "placeholder": "Titulo"}
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control pl-5", "placeholder": "Descripción"}
        )
    )

    assignee_by = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput(attrs={"class": "form-control pl-5"}),
    )
    assignee = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={"class": "form-control pl-5"}),
    )

    group = forms.ModelChoiceField(
        queryset=GroupHitman.objects.all(),
        widget=forms.Select(attrs={"class": "form-control pl-5"}),
    )

    status = forms.ChoiceField(
        choices=StatusType.choices(),
        widget=forms.HiddenInput(attrs={"class": "form-control pl-5"}),
    )

    class Meta:
        model = Hit
        fields = "__all__"
