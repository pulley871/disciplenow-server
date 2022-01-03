from rest_framework import serializers

from disciplenowapi.models import DiscipleGroup, Disciple, DiscipleToGroup, Entry
from django.contrib.auth.models import User

from disciplenowapi.models.message import Message


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ("id", "hear", "engage", "apply",
                  "respond", "date", "reference")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class NeedToContactSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Disciple
        fields = ("id", "user", "has_posted")


class MessageContact(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Disciple
        fields = ("id", "user")


class MessageSerializer(serializers.ModelSerializer):
    lead_disciple = MessageContact(many=False)

    class Meta:
        model = Message
        fields = ("id", "date", "body", "is_read", "lead_disciple")


class DiscipleSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    entries = EntrySerializer(many=True)
    messages = MessageSerializer(many=True)

    class Meta:
        model = Disciple
        messages = MessageSerializer(many=True)
        fields = ("id", "has_posted", "user", "entries", "is_lead", "messages")


class DiscipleGroupSerializer(serializers.ModelSerializer):
    group_disciples = DiscipleSerializer(many=True)

    class Meta:
        model = DiscipleGroup
        fields = ("id", "lead_disciple", "group_type", "group_disciples")


class LeadSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    entries = EntrySerializer(many=True)
    messages = MessageSerializer(many=True)

    class Meta:
        model = Disciple
        fields = ("id", "is_lead", "has_posted", "user", "entries", "messages")
