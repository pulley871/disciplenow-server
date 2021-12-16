from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DateField
from django.db.models.fields.related import ForeignKey


class Message(models.Model):
    """Defines Message Model"""
    lead_disciple = ForeignKey(
        "Disciple", on_delete=CASCADE, related_name="sent_messages")
    disciple = ForeignKey("Disciple", on_delete=CASCADE,
                          related_name="received_messages")
    body = CharField(max_length=200)
    date = DateField(default="2021-01-01")
    is_read = BooleanField(default=False)
