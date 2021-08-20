# Django Core
from django.db import models


class HitsAssignee(models.Manager):
    def get_queryset(self):
        return self.prefetch_related("assignee")
