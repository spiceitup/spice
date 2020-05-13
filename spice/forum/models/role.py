from django.db import models
from spice.common.auditing_entity import AuditingEntity
from spice.forum.models.admin import Admin


class Role(AuditingEntity):
    id = models.OneToOneField(Admin, primary_key=True, editable=False, on_delete=models.CASCADE)
