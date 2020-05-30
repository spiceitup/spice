from django.db import models
from spice.common.auditing_entity import AuditingEntity
from spice.forum.models.post import Post
from spice.common.enum.vote_type import VoteType


class Vote(AuditingEntity):
    id = models.DecimalField(primary_key=True, editable=False, max_digits=19, decimal_places=10)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vote_type = models.CharField(
        choices=[(type, type.value) for type in VoteType],
        max_length=250
    )
