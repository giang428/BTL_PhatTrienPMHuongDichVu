from django.shortcuts import render
from .models import History
from user.models import User
from django.db.models import Q
import datetime
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def getlistHistory(request,id):
    u=User.objects.get(id_user=id)
    listHist=History.objects.filter(user=u)
    if listHist:
        data=list(listHist.values())
        return Response({"data":data,"message":"Success","code":status.HTTP_200_OK},status=status.HTTP_200_OK)
    return Response({"data":[],"message":"Failed","code":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)