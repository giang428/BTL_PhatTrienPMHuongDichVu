from django.shortcuts import render
from django.db.models import Q
import datetime
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from mediareaction.models import MediaReaction
from user.models import User
from .models import HistoryMedia

@api_view(['POST'])
def post_history_media(request):
    id_media=request.GET.get('id_media')
    id_user=request.GET.get('id_user')
    user=User.objects.get(id_user=id_user)
    type_media=request.GET.get('type_media')
    # day_watch=request.GET.get('day_watch')
    duration=request.GET.get('duration')
    if id_media and user and type_media and duration:
        histMedia=HistoryMedia(id_media=id_media,user=user,type_media=type_media,duration=duration,day_watch=datetime.datetime.now())
        histMedia.save()
        return Response({"message":"Success"},status=status.HTTP_201_CREATED)
    return Response({"message":"Failed"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_list_history_media_by_userid(request,id_user):
    user=User.objects.get(id_user=id_user)
    list_histMedia=HistoryMedia.objects.filter(user=user)
    if list_histMedia:
        return Response({"data":list(list_histMedia.values())},status=status.HTTP_200_OK)
    return Response({"data":[]},status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_history_media(request):
    id_media=request.GET.get('id_media')
    id_user=request.GET.get('id_user')
    user=User.objects.get(id_user=id_user)
    duration=request.GET.get('duration')
    day_watch=request.GET.get('day_watch')
    if id_media and user:
        histMedia=HistoryMedia.objects.get(Q(id_media=id_media) & Q(user=user))
        if day_watch:
            histMedia.set_day_watch(day_watch)
        if duration:
            histMedia.set_duration(duration)
        histMedia.save()
        return Response({"message":"Success"},status=status.HTTP_202_ACCEPTED)
    return Response({"message":"Failed"},status=status.HTTP_400_BAD_REQUEST)
    