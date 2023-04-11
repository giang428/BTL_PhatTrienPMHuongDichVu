from django.urls import path
from historymedia import views

urlpatterns = [
    path("createhistorymedia",views.post_history_media,name="createhistorymedia"),
    path("getlisthistorybyuserid/<int:id_user>",views.get_list_history_media_by_userid,name="getlisthistorybyuserid"),
    path("updatehistorymedia",views.update_history_media,name="updatehistorymedia"),
]
