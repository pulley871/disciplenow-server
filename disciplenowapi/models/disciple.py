from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ManyToManyField, OneToOneField
from django.contrib.auth.models import Group, User
from datetime import datetime, timedelta
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

    @property
    def has_posted(self):
        end_date = datetime.now()
        start_date = datetime.now() - timedelta(days=5)
        entries = Entry.objects.filter(disciple__user=self.user)
        checker = 0
        for entry in entries:
            converted_date = datetime(entry.date.year,entry.date.month,entry.date.day)
            if start_date <= converted_date  <= end_date:
                checker += 1
        if checker >= 1:
            return True
        else:
            return False