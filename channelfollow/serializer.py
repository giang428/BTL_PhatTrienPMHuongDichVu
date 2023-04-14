from .models import ChannelFollow
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelFollow
        fields=("id_follow","id_channel","id_user","day_follow")