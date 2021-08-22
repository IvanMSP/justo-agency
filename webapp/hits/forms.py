# DJANGO CORE IMPORTS
from django import forms
from django.db.models import Q

# Onwer
from hits.models import Hit
from accounts.models import User
from reusable.choices import StatusType


class HitForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(HitForm, self).__init__(*args, **kwargs)
        instance = getattr(self, "instance", None)
        if instance and instance.id:
            if self.user.is_hitman is True:
                self.fields["title"].widget.attrs["readonly"] = True
                self.fields["description"].widget.attrs["readonly"] = True
                self.fields["assignee_by"].widget.attrs["disabled"] = True
                self.fields["assignee"].widget.attrs["disabled"] = True
                self.fields["status"].choices = StatusType.choices_hitman()

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
        queryset=User.objects.filter(Q(is_boss=True) | Q(is_manager=True)),
        widget=forms.Select(attrs={"class": "form-control pl-5"}),
    )
    assignee = forms.ModelChoiceField(
        queryset=User.objects.filter(Q(is_hitman=True) | Q(is_manager=True)),
        widget=forms.Select(attrs={"class": "form-control pl-5"}),
    )

    status = forms.ChoiceField(
        choices=StatusType.choices(),
        widget=forms.Select(attrs={"class": "form-control pl-5"}),
    )

    class Meta:
        model = Hit
        fields = "__all__"
