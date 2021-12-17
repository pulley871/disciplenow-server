from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from disciplenowapi.models import Disciple, DiscipleGroup
from datetime import datetime, timedelta
from .serializers import LeadSerializer, DiscipleGroupSerializer, DiscipleSerializer, NeedToContactSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def lead_dashboard(request):
    try:
        lead_disciple = Disciple.objects.get(
            user=request.auth.user, is_lead=True)
        group = DiscipleGroup.objects.get(lead_disciple=lead_disciple)
        failed_to_post = []
        lead_sent_message = lead_disciple.sent_messages.all()
        end_date = datetime.now()
        start_date = datetime.now() - timedelta(days=5)
        for disciple in group.group_disciples.all():
            for message in lead_sent_message:
                converted_date = datetime(
                    message.date.year, message.date.month, message.date.day)
                if message.disciple == disciple and start_date <= converted_date <= end_date:
                    pass
                elif disciple.has_posted == False:
                    failed_to_post.append(disciple)
        failed_to_post = NeedToContactSerializer(
            failed_to_post, many=True, context={"request": request})
        lead_disciple = LeadSerializer(
            lead_disciple, many=False, context={"request": request})
        group = DiscipleGroupSerializer(
            group, many=False, context={"request": request})
        return Response({"lead_disciple": lead_disciple.data, "group": group.data, "need_to_contact": failed_to_post.data}, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
