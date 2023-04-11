from django.shortcuts import render
from history.models import History
from django.db.models import Q
import datetime
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializer import UserSerializer
def get_id_by_username_password(username, password):
    listU=User.objects.all()
    for u in listU:
        if u.username==username and u.password==password:
            return u.id_user
    return None
@api_view(['POST'])
def register_user(request):
    listUser=User.objects.all()
    check_user=False
    data=request.GET
    print(data.get('username'))
    user=User(username=data.get('username'), password=data.get('password'),full_name=data.get('full_name'),address=data.get('address'),phone=data.get('phone'),gender=data.get('gender'))
    if check_user==False:
        for u in listUser:
            if u.username==user.username and u.password==user.password:
                check_user=True
                user.set_id(u.id_user)
    if check_user:
        return Response({"message":"Invalid"})
    else:
        if user:
            # hist=History(exp_vip=datetime.datetime.now(),user=user)
            user.save()#{"id":get_id_by_username_password(user.username,user.password),"username":user.username,"password":user.password}}
            # hist.save()
            return Response({"message":"Success","id_user":user.id_user},status=status.HTTP_201_CREATED)
        return Response({"message":"Failded"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user(request,id):
    user=User.objects.get(id_user=id)
    # full_name=models.CharField(max_length=200,null=True)
    # address=models.CharField(max_length=200,null=True)
    # phone=models.CharField(max_length=200,null=True)
    # gender=models.CharField(max_length=200,null=True)
    # role=models.CharField(max_length=200,default="member")
    if user:
        if request.GET.get('full_name'):
            user.set_fullname(request.GET.get('full_name'))
        if request.GET.get('role'):
            user.set_role(request.GET.get('role'))
        if request.GET.get('address'):
            user.set_address(request.GET.get('address'))
        if request.GET.get('phone'):
            user.set_phone(request.GET.get('phone'))
        if request.GET.get('gender'):
            user.set_gender(request.GET.get('gender'))
        
        user.save()
        return Response({"message":"Success"},status=status.HTTP_202_ACCEPTED)
    return Response({"message":"Failed"},status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_users(request):
    data = User.objects.all()
    if data:
        list_user = list(data.values())
        return Response(list_user,status=status.HTTP_200_OK)
    return Response({"message":"Failed fetching data from server"})
@api_view(['PUT'])
def update_vip_user(request):
    id_user=request.GET.get('is_user')
    is_vip=request.GET.get('is_vip')
    user=User.objects.get(id_user=id_user)
    if user and is_vip:
        user.set_is_vip(is_vip)
        user.save()
        hist=History(exp_vip=datetime.datetime.now(),is_vip=is_vip,user=user)
        hist.save()
        return Response({"message": "Success"},status=status.HTTP_202_ACCEPTED)
    return Response({"message": "Failed"},status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login(request):
    data=request.GET
    uname=data.get('username')
    passw=data.get('password')
    listU=User.objects.all()
    for u in listU:
        if u.username==uname and u.password==passw:
            # hist=History.objects.get(Q(user_id=u.id_user) & Q(is_active=True))
            return Response({"data":{"id":u.id_user,"username":u.username,"password":u.password,"full_name":u.full_name,"address":u.address,"phone":u.phone,"gender":u.gender,"role":u.role,"is_vip":u.is_vip},"message":"Success"},status=status.HTTP_200_OK)
    return Response({"data":{"id":None,"username":None,"password":None,"full_name":None,"address":None,"phone":None,"gender":None,"role":None,"is_vip":None},"message":"Failed"},status=status.HTTP_400_BAD_REQUEST)