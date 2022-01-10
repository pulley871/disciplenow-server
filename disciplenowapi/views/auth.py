from os import stat
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from disciplenowapi.models import Disciple, DiscipleGroup
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import LeadSerializer, DiscipleGroupSerializer, DiscipleSerializer, NeedToContactSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    try:
        user = authenticate(
            username=request.data["userName"], password=request.data["password"])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"token": token.key, "valid": True}, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"message": "Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
