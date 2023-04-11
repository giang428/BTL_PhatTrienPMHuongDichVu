from django.db import models
from user.models import User
import datetime
# Create your models here.
class History(models.Model):
    id=models.AutoField(primary_key=True)
    exp_vip=models.CharField(max_length=200)
    is_vip=models.CharField(max_length=200)
    # is_active=models.BooleanField(default=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)