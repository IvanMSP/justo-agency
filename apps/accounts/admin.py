# Django Core
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

# Owner
from .models import User, ProfileHitman, GroupHitman
from .forms.admin import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email"]
    list_filter = ["email", "is_boss", "is_manager", "is_hitman"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Datos personales",
            {"fields": ("first_name", "last_name", "bio", "status")},
        ),
        (
            "Permisos",
            {"fields": ("is_boss", "is_manager", "is_hitman", "is_staff")},
        ),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "bio",
                    "status",
                    "is_boss",
                    "is_manager",
                    "is_hitman",
                    "is_staff",
                ),
            },
        ),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(GroupHitman)
admin.site.register(ProfileHitman)
