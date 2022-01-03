from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from disciplenowapi.models import Disciple, DiscipleGroup
from disciplenowapi.views.serializers.serializers import DiscipleSerializer



class DiscipleView(ViewSet):
    """Api view for Disciples"""
    def list(self,request):
        try:
            lead_disciple = Disciple.objects.get(user=request.auth.user, is_lead=True)
            group = DiscipleGroup.objects.get(lead_disciple=lead_disciple)
            search_term = self.request.query_params.get("searchterm",None)
            if search_term is not None:
                disciples = Disciple.objects.filter(user__email__contains=search_term).exclude(groups=group)
                
                
            data = DiscipleSerializer(disciples, many=True, context={"request":request})
            return Response(data.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)