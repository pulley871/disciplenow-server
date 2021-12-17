from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from disciplenowapi.models import Disciple
from disciplenowapi.views.serializers import DiscipleSerializer
from django.contrib.auth.models import User


class DiscipleView(ViewSet):
    """API View for Non-Lead users"""

    def retrieve(self, request, pk):
        try:
            disciple = Disciple.objects.get(user=request.auth.user, pk=pk)
            data = DiscipleSerializer(
                disciple, many=False, context={"request": request})
            return Response(data.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk):
        try:
            disciple = Disciple.objects.get(user=request.auth.user, pk=pk)
            user_info = User.objects.get(pk=pk)
            user_info.first_name = request.data["first_name"]
            user_info.last_name = request.data["last_name"]
            user_info.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
