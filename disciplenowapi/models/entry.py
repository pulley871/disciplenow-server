from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey


class Entry(models.Model):
    """Defines Entry Model"""
    hear = CharField(max_length=500)
    engage = CharField(max_length=500)
    apply = CharField(max_length=500)
    respond = CharField(max_length=500)
    reference = CharField(max_length=20)
    date = DateField(default="2021-01-01")
    disciple = ForeignKey("Disciple", on_delete=CASCADE)
