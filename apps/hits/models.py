# Django core Libraries
from django.db import models

# Owner Libraries
from accounts.models import User
from apps.reusable.constants import BLANK, REQUIRED
from reusable.models import TimeStampModel


class Hit(TimeStampModel):
    title = models.CharField(max_length=120, verbose_name="Titulo", **REQUIRED)
    description = models.TextField(verbose_name="Descripcioón", **BLANK)
    status = models.BooleanField(verbose_name="Estatus", default=True)
    assignee_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="hits_assignee_by",
        verbose_name="Asignado por",
        **REQUIRED
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="hits_assignee",
        verbose_name="Asignados",
        **REQUIRED
    )

    def __str__(self) -> str:
        return self.title
