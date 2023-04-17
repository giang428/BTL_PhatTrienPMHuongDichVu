import json
from django.shortcuts import render
from django.db.models import Q
import datetime
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import MediaReaction
from user.models import User
from historymedia.models import HistoryMedia
# Create your views here.

@api_view(['POST'])
def post_media_reaction(request):
    id_media=request.GET.get('id_media')
    id_user=request.GET.get('id_user')
    user=User.objects.get(id_user=id_user)
    day_reaction=datetime.date.today()
    type_media=request.GET.get('type_media')
    type_reaction=request.GET.get('type_reaction')
    type_favorite=request.GET.get('type_favorite')
    if id_media and user and day_reaction and type_media and type_reaction and type_favorite:
        media_reaction = MediaReaction(id_media=id_media,user=user,day_reaction=day_reaction,type_media=type_media,type_reaction=type_reaction,type_favorite=type_favorite)
        media_reaction.save()
        return Response({"message":"Success"},status=status.HTTP_201_CREATED)
    return Response({"message":"Failed"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_media_reaction(request):
    id_media=request.GET.get('id_media')
    id_user=request.GET.get('id_user')
    user=User.objects.get(id_user=id_user)
    if id_media and user:
        histMedia=HistoryMedia.objects.filter(id_media=id_media)
        listLikeMediaReaction=MediaReaction.objects.filter(Q(id_media=id_media) & Q(type_reaction=1))
        listDisLikeMediaReaction=MediaReaction.objects.filter(Q(id_media=id_media) & Q(type_reaction=2))
        media_user_reaction=MediaReaction.objects.filter(Q(id_media=id_media) & Q(user=user))
        if media_user_reaction:
            return Response({"id_mreaction":media_user_reaction[0].id_mreaction,"favorite":media_user_reaction[0].type_favorite,"reactionUser":media_user_reaction[0].type_reaction,"amountLike":len(listLikeMediaReaction),"amountDisLike":len(listDisLikeMediaReaction),"countView":len(histMedia)},status=status.HTTP_200_OK)
        return Response({"id_mreaction":-1,"favorite":0,"reactionUser":0,"amountLike":len(listLikeMediaReaction),"amountDisLike":len(listDisLikeMediaReaction),"countView":len(histMedia)},status=status.HTTP_200_OK)
    return Response({"id_mreaction":-1,"favorite":-1,"reactionUser":-1,"amountLike":-1,"amountDisLike":-1,"countView":len(histMedia)},status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def thongke_app(request):
    listLikeapp=MediaReaction.objects.filter(Q(type_reaction=1))
    listDisLikeapp=MediaReaction.objects.filter(Q(type_reaction=2))
    listfavoriteapp=MediaReaction.objects.filter(Q(type_favorite=1))
    listviewapp=HistoryMedia.objects.all()
    data={"countLikeApp":len(listLikeapp),"countDisLikeApp":len(listDisLikeapp),"countViewApp":len(listviewapp),"countFavoriteApp":len(listfavoriteapp)}
    return Response({"data":data,"code":200,"message":"Success"},status=status.HTTP_200_OK)
@api_view(['GET'])
def thongke_media_byid(request,id_media):
    histMedia=HistoryMedia.objects.filter(id_media=id_media)
    listLikeMediaReaction=MediaReaction.objects.filter(Q(id_media=id_media) & Q(type_reaction=1))
    listDisLikeMediaReaction=MediaReaction.objects.filter(Q(id_media=id_media) & Q(type_reaction=2))
    return Response({"id_media":id_media,"countView":len(histMedia),"countLike":len(listLikeMediaReaction),"countDisLike":len(listDisLikeMediaReaction),"countViewApp":len(HistoryMedia.objects.all())},status=status.HTTP_200_OK)
    
@api_view(['GET'])
def getListFavoriteMediaReaction(request,id_user):
    type_media=request.GET.get('type_media')
    user=User.objects.get(id_user=id_user)
    listFavoriteMedia_User=MediaReaction.objects.filter(Q(user=user) & Q(type_favorite=1) & Q(type_media=type_media))
    if listFavoriteMedia_User:
        return Response({"data":list(listFavoriteMedia_User.values())},status=status.HTTP_200_OK)
    return Response({"data":[]},status=status.HTTP_200_OK)
    
@api_view(['PUT'])
def update_media_reaction(request):
    id_mreaction=request.GET.get('id_mreaction')
    type_favorite=request.GET.get('type_favorite')
    type_reaction=request.GET.get('type_reaction')
    media_reaction=MediaReaction.objects.get(id_mreaction=id_mreaction)
    if media_reaction:
        if type_reaction:
            media_reaction.set_type_favorite(type_favorite)
        if type_favorite:
            media_reaction.set_type_reaction(type_reaction)
        media_reaction.save()
        return Response({"message":"Success"},status=status.HTTP_202_ACCEPTED)
    return Response({"message":"Failed"},status=status.HTTP_400_BAD_REQUEST)
        
            