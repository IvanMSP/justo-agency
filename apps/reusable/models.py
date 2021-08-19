# Django
from django.db import models


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now=True, verbose_name="creado")
    modified = models.DateTimeField(auto_now_add=True, verbose_name="modificado")

    class Meta:
        abstract = True
