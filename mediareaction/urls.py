from django.urls import path
from mediareaction import views

urlpatterns = [
    path("createMediaReaction",views.post_media_reaction,name="createMediaReaction"),
    path("getMediaReaction",views.get_media_reaction,name="getMediaReaction"),
    path("getlistmediafavorite/<int:id_user>",views.getListFavoriteMediaReaction,name="getListFavoriteMediaReaction"),
    path("updateMediaReaction",views.update_media_reaction,name="updateMediaReaction"),
    path("thongkemedia/<str:id_media>",views.thongke_media_byid,name="thongkemedia"),
    path("thongkeapp",views.thongke_app,name="thongkeapp"),
]
