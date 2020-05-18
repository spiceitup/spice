from django.db import models
from spice.common.auditing_entity import AuditingEntity
from spice.account.models.user import User
from .forum import Forum


class Post(AuditingEntity):
    id = models.DecimalField(primary_key=True, editable=False, max_digits=19, decimal_places=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
