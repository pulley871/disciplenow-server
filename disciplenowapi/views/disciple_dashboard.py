from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from disciplenowapi.models import Disciple, DiscipleGroup

from .serializers import LeadSerializer, DiscipleGroupSerializer, DiscipleSerializer, NeedToContactSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def disciple_home(request):
    try:
        disciple = Disciple.objects.get(user=request.auth.user)
        data = DiscipleSerializer(
            disciple, many=False, context={"request": request})
        return Response(data.data, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
