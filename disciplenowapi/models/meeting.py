from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, TimeField
from django.db.models.fields.related import ForeignKey


class Meeting(models.Model):
    """Model for the meeting"""
    label = CharField(max_length=200)
    time = TimeField()
    date = DateField(default="2021-01-01")
    group = ForeignKey("DiscipleGroup", on_delete=CASCADE)
