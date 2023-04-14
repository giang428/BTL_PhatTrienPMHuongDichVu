from django.urls import path
from channelfollow import views

urlpatterns = [
    path("follow",views.follow,name="follow"),
    path("check/follow",views.checkfollow,name="checkfollow"),
    path("unfollow",views.unfollow,),
]