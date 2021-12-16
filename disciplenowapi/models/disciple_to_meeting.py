from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


class DiscipleToMeeting(models.Model):
    """Brdige Table For Disciple to Meetings"""
    disciple = ForeignKey("Disciple", on_delete=CASCADE)
    meeting = ForeignKey("Meeting", on_delete=CASCADE)
