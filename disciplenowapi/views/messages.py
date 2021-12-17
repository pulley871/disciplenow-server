from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from disciplenowapi.models import Disciple, Message, disciple
from disciplenowapi.views.serializers import MessageSerializer


class MessageView(ViewSet):
    """View for messages for disciples"""

    def create(self, request):
        try:
            lead_disciple = Disciple.objects.get(
                user=request.auth.user, is_lead=True)
            message_recipient = Disciple.objects.get(
                pk=request.data["recipient_id"])
            Message.objects.create(
                lead_disciple=lead_disciple,
                disciple=message_recipient,
                body=request.data["message_body"],
                date=request.data["date"],
                is_read=False
            )
            return Response({"message": "Message Sent"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk):
        try:
            message = Message.objects.get(pk=pk)
            data = MessageSerializer(
                message, many=False, context={"request": request})
            return Response(data.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk):
        try:
            message = Message.objects.get(pk=pk)
            message.is_read = True
            message.save()
            data = MessageSerializer(
                message, many=False, context={"request": request})
            return Response(data.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
