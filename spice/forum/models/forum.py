from django.db import models
from common.auditing_entity import AuditingEntity
from django.contrib.auth import get_user_model

User = get_user_model()

class Forum(AuditingEntity):
    id = models.DecimalField(primary_key=True, editable=False, max_digits=19, decimal_places=10)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    subscribers = models.ManyToManyField(User, blank=True)
