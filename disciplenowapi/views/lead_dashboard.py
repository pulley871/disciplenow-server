from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from disciplenowapi.models import Disciple, DiscipleGroup

from .serializers import LeadSerializer, DiscipleGroupSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def lead_dashboard(request):
    try:
        lead_disciple = Disciple.objects.get(user=request.auth.user)
        group = DiscipleGroup.objects.get(lead_disciple=lead_disciple)
        # for disciple in group.group_disciples.all():
        #     disciple.entry = disciple.entry_set.all()

        lead_disciple = LeadSerializer(
            lead_disciple, many=False, context={"request": request})
        group = DiscipleGroupSerializer(
            group, many=False, context={"request": request})
        return Response({"lead_disciple": lead_disciple.data, "group": group.data}, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
