import uuid

from django.db import models
from spice.common.auditing_entity import AuditingEntity


class User(AuditingEntity):
    id = models.DecimalField(primary_key=True, editable=False, max_digits=19, decimal_places=10)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    super_user = models.BooleanField()
