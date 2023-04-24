from django.urls import path

from history import views

urlpatterns=[
    path("getlistHistorybyuserid/<int:id>",views.getlistHistory,name="getlistHistorybyuserid"),
    path("stat",views.stat,name="statistic"),
    path("statall",views.stat_all,name="stat_all")
]