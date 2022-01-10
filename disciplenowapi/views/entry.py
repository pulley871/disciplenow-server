from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from disciplenowapi.models import Disciple, DiscipleGroup, Message, disciple, Entry
from datetime import date, datetime


class EntryView(ViewSet):
    """View for entries"""

    def create(self, request):
        try:
            disciple = Disciple.objects.get(user=request.auth.user)
            date = datetime.now().strftime('%Y-%m-%d')
            Entry.objects.create(
                hear=request.data["hear"],
                engage=request.data["engage"],
                apply=request.data["apply"],
                respond=request.data["respond"],
                reference=request.data["reference"],
                date=date,
                disciple=disciple
            )
            return Response({"Message": "Entry Saved"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
