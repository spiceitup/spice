from django.db import models


class AuditingEntity(models.Model):
    modified_date = models.DateTimeField()
    created_date = models.DateTimeField()

    class Meta:
        abstract = True
