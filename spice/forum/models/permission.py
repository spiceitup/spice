import uuid

from django.db import models
from spice.common.auditing_entity import AuditingEntity
from .role import Role


class Permission(AuditingEntity):
    id = models.DecimalField(primary_key=True, editable=False, max_digits=19, decimal_places=10)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
