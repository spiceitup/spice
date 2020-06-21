from django.db import models
from spice.common.auditing_entity import AuditingEntity
from django.contrib.auth import get_user_model

User = get_user_model()


class Admin(AuditingEntity):
    id = models.DecimalField(primary_key=True, editable=False, max_digits=19,
                             decimal_places=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum_id = models.DecimalField(max_digits=19, decimal_places=10)
    role_id = models.DecimalField(max_digits=19, decimal_places=10)
