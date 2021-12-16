from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class DiscipleToGroup(models.Model):
    """Bridge Tabel for disciple to group"""
    disciple = ForeignKey("Disciple", on_delete=CASCADE)
    group = ForeignKey("DiscipleGroup", on_delete=CASCADE)
