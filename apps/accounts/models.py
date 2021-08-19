# Django core Libraries
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import manager
from django.db.models.deletion import PROTECT

# Owner's Libraries
from apps.reusable.constants import REQUIRED
from .managers import UserManager
from reusable.models import TimeStampModel


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.EmailField(unique=True, **REQUIRED)
    first_name = models.CharField(max_length=150, **REQUIRED)
    last_name = models.CharField(max_length=150, **REQUIRED)
    bio = models.TextField(**REQUIRED)
    status = models.BooleanField(default=True)
    is_boss = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_hitman = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".title()


class GroupHitman(TimeStampModel):
    name = models.CharField(max_length=120, verbose_name="Nombre del grupo", **REQUIRED)
    description = models.TextField(verbose_name="Descripción del grupo", **REQUIRED)
    boss = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="groups_boss",
        verbose_name="Boss",
        **REQUIRED,
    )
    manager_group = models.OneToOneField(
        User, on_delete=models.PROTECT, verbose_name="Manager", **REQUIRED
    )

    class Meta:
        verbose_name = "Grupo Hitman"
        verbose_name_plural = "Grupos Hitman"

    def __str__(self):
        return self.name


class ProfileHitman(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    group_hitman = models.ForeignKey(
        GroupHitman,
        on_delete=PROTECT,
        related_name="hitmans",
        verbose_name="Grupo",
        **REQUIRED,
    )

    class Meta:
        verbose_name = "Hitman"
        verbose_name_plural = "Hitmans"

    def __str__(self):
        return self.user.get_full_name()
