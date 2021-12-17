from rest_framework import serializers

from disciplenowapi.models import DiscipleGroup, Disciple, DiscipleToGroup, Entry, Message
from django.contrib.auth.models import User


class EntrySerializer(serializers.ModelSerializer):
    """Basic Entry Serializer"""
    class Meta:
        model = Entry
        fields = ("id", "hear")


class UserSerializer(serializers.ModelSerializer):
    """First and Last name User Serializer"""
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class NeedToContactSerializer(serializers.ModelSerializer):
    """Lead Disciple list of users that need contacting, same as disciple serializer minus entries"""
    user = UserSerializer(many=False)

    class Meta:
        model = Disciple
        fields = ("id", "user", "has_posted")


class DiscipleSerializer(serializers.ModelSerializer):
    """Basic Disciple Serializer with entries"""
    user = UserSerializer(many=False)
    entries = EntrySerializer(many=True)

    class Meta:
        model = Disciple
        fields = ("id", "has_posted", "user", "entries", "received_messages")


class MessageSerializer(serializers.ModelSerializer):
    """Message Serailizer """
    lead_disciple = NeedToContactSerializer(many=False)

    class Meta:
        model = Message
        fields = ("id", "body", "date", "is_read", "lead_disciple")


class DiscipleGroupSerializer(serializers.ModelSerializer):
    """Serializer to for disciple groups and to provide users in specifc group for data pull"""
    group_disciples = DiscipleSerializer(many=True)

    class Meta:
        model = DiscipleGroup
        fields = ("id", "lead_disciple", "group_type", "group_disciples")


class LeadSerializer(serializers.ModelSerializer):
    """Serializer for Lead Disciple"""
    user = UserSerializer(many=False)

    class Meta:
        model = Disciple
        fields = ("id", "is_lead", "has_posted", "user")
