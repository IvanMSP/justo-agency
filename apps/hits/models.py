# Django core Libraries
from apps.accounts.managers import HitmanManager
from django.db import models

# Owner Libraries
from accounts.models import User
from apps.reusable.constants import BLANK, REQUIRED
from reusable.models import TimeStampModel
from reusable.choices import StatusType


class Hit(TimeStampModel):
    title = models.CharField(max_length=120, verbose_name="Titulo", **REQUIRED)
    description = models.TextField(verbose_name="Descripción", **BLANK)
    status = models.PositiveSmallIntegerField(
        verbose_name="Estatus", choices=StatusType.choices()
    )
    assignee_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="assignee_by",
        verbose_name="Asignado por",
        **REQUIRED
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="assignee",
        verbose_name="Asignados",
        **REQUIRED
    )

    def __str__(self) -> str:
        return self.title
