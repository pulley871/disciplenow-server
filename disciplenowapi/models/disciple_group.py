from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class DiscipleGroup(models.Model):
    """Defines Disciple Group Models"""
    lead_disciple = ForeignKey("Disciple", on_delete=CASCADE)
    group_type = ForeignKey("GroupType", on_delete=CASCADE)
