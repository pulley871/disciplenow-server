from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from disciplenowapi.models import Disciple, DiscipleGroup

from .serializers import LeadSerializer, DiscipleGroupSerializer, DiscipleSerializer, NeedToContactSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def is_lead_check(request):
    try:
        disciple = Disciple.objects.get(user=request.auth.user)
        if disciple.is_lead:
            return Response({"check": True}, status=status.HTTP_200_OK)
        else:
            return Response({"check": False}, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
