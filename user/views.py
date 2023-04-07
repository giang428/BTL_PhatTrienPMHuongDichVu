from django.shortcuts import render

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
            user.save()#{"id":get_id_by_username_password(user.username,user.password),"username":user.username,"password":user.password}}
                    
            return Response({"message":"Successfully"},status=status.HTTP_201_CREATED)
        return Response({"message":"Failded"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_vip_user(request,id):
    u=User.objects.get(id_user=id)
    if u and u.is_vip==False:
        u.set_is_vip(True)
        u.save()
        return Response({"message":"Successfully"},status=status.HTTP_205_RESET_CONTENT)
    return Response({"message":"Error update"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    data=request.GET 
    uname=data.get('username')
    passw=data.get('password')
    listU=User.objects.all()
    for u in listU:
        if u.username==uname and u.password==passw:
            return Response({"data":{"id":u.id_user,"username":u.username,"password":u.password},"message":"Login Success"},status=status.HTTP_200_OK)
    return Response({"data":{"id":None,"username":None,"password":None},"message":"Login Failed"},status=status.HTTP_400_BAD_REQUEST)