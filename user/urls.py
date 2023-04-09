from django.urls import path
from user import views

urlpatterns = [
    path("register_user",views.register_user,name="register_user"),
    path("update_vip_user/<int:id>",views.update_vip_user,name="update_vip_user"),
    path("login",views.login,name="login"),
    path("get_users/",views.get_users,name="get_user")
]