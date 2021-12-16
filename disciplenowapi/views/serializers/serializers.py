from rest_framework import serializers

from disciplenowapi.models import DiscipleGroup, Disciple, DiscipleToGroup, Entry
from django.contrib.auth.models import User


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ("id", "hear")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class DiscipleSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    entries = EntrySerializer(many=True)

    class Meta:
        model = Disciple
        fields = ("id", "has_posted", "user", "entries")


class DiscipleGroupSerializer(serializers.ModelSerializer):
    group_disciples = DiscipleSerializer(many=True)

    class Meta:
        model = DiscipleGroup
        fields = ("id", "lead_disciple", "group_type", "group_disciples")


class LeadSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Disciple
        fields = ("id", "is_lead", "has_posted", "user")
