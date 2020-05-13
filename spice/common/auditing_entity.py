from django.db import models


class AuditingEntity(models.Model):
    modified_date = models.DateField()
    created_date = models.DateField()

    class Meta:
        abstract = True
