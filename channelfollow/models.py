from django.db import models
from user.models import User

class ChannelFollow(models.Model):
    id_follow=models.AutoField(primary_key=True)
    id_channel=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    day_follow=models.DateField()
