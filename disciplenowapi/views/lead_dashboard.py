from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from disciplenowapi.models import Disciple, DiscipleGroup

from .serializers import LeadSerializer, DiscipleGroupSerializer, DiscipleSerializer, NeedToContactSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def lead_dashboard(request):
    try:
        lead_disciple = Disciple.objects.get(
            user=request.auth.user, is_lead=True)

        group = DiscipleGroup.objects.get(lead_disciple=lead_disciple)

        failed_to_post = []
        for disciple in group.group_disciples.all():
            if disciple.has_posted == False:
                failed_to_post.append(disciple)
        failed_to_post = NeedToContactSerializer(
            failed_to_post, many=True, context={"request": request})
        lead_disciple = LeadSerializer(
            lead_disciple, many=False, context={"request": request})
        group = DiscipleGroupSerializer(
            group, many=False, context={"request": request})
        return Response({"lead_disciple": lead_disciple.data, "group": group.data, "need_to_contact": failed_to_post.data}, status=status.HTTP_200_OK)
    except DiscipleGroup.DoesNotExist:
        lead_disciple = Disciple.objects.get(
            user=request.auth.user, is_lead=True)
        data = LeadSerializer(lead_disciple, many=False,
                              context={"request": request})
        return Response(data.data, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["Get"])
@permission_classes([IsAuthenticated])
def selected_disciple(request, pk):
    try:
        lead_disciple = Disciple.objects.get(
            user=request.auth.user, is_lead=True)
        group = DiscipleGroup.objects.get(lead_disciple=lead_disciple)
        selected_disciple = Disciple.objects.get(pk=pk)
        data = DiscipleSerializer(
            selected_disciple, many=False, context={"request": request})
        return Response(data.data, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"Message": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def promote_selected_disciple(request, pk):
    try:
        lead_disciple = Disciple.objects.get(
            user=request.auth.user, is_lead=True)
        if lead_disciple is not None:
            disciple = Disciple.objects.get(pk=pk)
            disciple.is_lead = True
            disciple.save()
            return Response({"Mesage": "Disciple Promoted"}, status=status.HTTP_204_NO_CONTENT)
    except Exception as ex:
        return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["Put"])
@permission_classes([IsAuthenticated])
def add_member_to_group(request):
    try:
        lead_disciple = Disciple.objects.get(
            user=request.auth.user, is_lead=True)
        group = DiscipleGroup.objects.get(lead_disciple=lead_disciple)
        disciple_array = []
        for disciple in group.group_disciples.all():

            disciple_array.append(disciple.id)
        if request.data["discipleId"] in disciple_array:
            disciple_array.remove(request.data["discipleId"])
        else:
            disciple_array.append(request.data["discipleId"])
        group.group_disciples.set(disciple_array)
        return Response({"Message": "Disciple Added"}, status=status.HTTP_201_CREATED)
    except Exception as ex:
        return Response({"Message": ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
