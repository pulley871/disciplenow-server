from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ManyToManyField, OneToOneField
from django.contrib.auth.models import User

from disciplenowapi.models.entry import Entry


class Disciple (models.Model):
    """Defines Disciple Class"""
    user = OneToOneField(User, on_delete=CASCADE)
    is_lead = BooleanField(default=False)
    has_posted = BooleanField(default=True)
    groups = ManyToManyField(
        "DiscipleGroup", through="DiscipleToGroup", related_name="group_disciples")
    meetings = ManyToManyField(
        "Meeting", through="DiscipleToMeeting", related_name="attending_disciples")

    @property
    def entries(self):
        return Entry.objects.filter(disciple__user=self.user)
