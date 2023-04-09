from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=("id_user","username","password","full_name","address","phone","gender","role","is_vip")