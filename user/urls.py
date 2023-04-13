from django.urls import path
from user import views

urlpatterns = [
    path("register_user",views.register_user,name="register_user"),
    path("update_user/<int:id>",views.update_user,name="update_user"),
    path("login",views.login,name="login"),
    path("get_users/",views.get_users,name="get_user"),
    path("update_vip_user",views.update_vip_user,name="update_vip_user"),
    path("thongkeacountvip/",views.getcountvip,name="thongkeacountvip"),
    path('userinfo/<int:id_user>',views.user_info_by_id,name="userinfo"),
]