from django.db import models
from common.auditing_entity import AuditingEntity
from .forum import Forum
from django.contrib.auth import get_user_model

User = get_user_model()



class Post(AuditingEntity):
    id = models.DecimalField(primary_key=True, editable=False, max_digits=19, decimal_places=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
