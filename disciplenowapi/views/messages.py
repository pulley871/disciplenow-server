from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from disciplenowapi.models import Disciple, DiscipleGroup, Message, disciple
from datetime import date, datetime

from disciplenowapi.views.serializers.serializers import MessageSerializer


class MessageView(ViewSet):
    """View for messages"""

    def create(self, request):
        """Sending Messages"""
        try:
            lead = Disciple.objects.get(user=request.auth.user)
            disciple = Disciple.objects.get(pk=request.data["discipleId"])
            Message.objects.create(
                lead_disciple=lead,
                disciple=disciple,
                body=request.data["body"],
                date=datetime.today().strftime('%Y-%m-%d'),
                is_read=False
            )
            return Response({"message": "Message sent!"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Get users messages"""
        try:
            disciple = Disciple.objects.get(user=request.auth.user)
            messages = Message.objects.filter(disciple=disciple)
            data = MessageSerializer(
                messages, many=True, context={"request": request})
            return Response(data.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
