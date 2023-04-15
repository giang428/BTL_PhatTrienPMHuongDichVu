from django.db.models import Q
import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from user.models import User
from .models import ChannelFollow

@api_view(['POST'])
def follow(request):
    id_channel=request.GET.get('id_channel')
    id_user=request.GET.get('id_user')
    user=User.objects.get(id_user=id_user)
    day_follow=datetime.date.today()
    if id_channel and user and day_follow:
        follow_channel = ChannelFollow(id_channel=id_channel,user=user,day_follow=day_follow)
        follow_channel.save()
        return Response({"data":"followed","code":200,"message":"Success"},status=status.HTTP_200_OK)
    return Response({"data":"none","code":400,"message":"Fail"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def checkfollow(request):
    data=request.GET
    id_channel=data.get('id_channel')
    id_user=data.get('id_user')
    user=User.objects.get(id_user=id_user)
    channelFollow=ChannelFollow.objects.filter(Q(id_channel=id_channel) & Q(user=user))
    if channelFollow:
        return Response({"data":"followed","code":200,"message":"Success"},status=status.HTTP_200_OK)
    return Response({"data":"none","code":404,"message":"Not Found"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def unfollow(request):
    data=request.GET
    id_channel=data.get('id_channel')
    id_user=data.get('id_user')
    user=User.objects.get(id_user=id_user)
    channelFollow=ChannelFollow.objects.filter(Q(id_channel=id_channel) & Q(user=user))
    if channelFollow:
        channelFollow.delete()
        return Response({"data":"unfollow","code":200,"message":"Success"},status=status.HTTP_200_OK)
    return Response({"data":"none","code":404,"message":"Not Found"},status=status.HTTP_400_BAD_REQUEST)
