from django.db import models
from django.db.models.fields import CharField


class GroupType(models.Model):
    """Defines Group Type"""
    label = CharField(max_length=40)
