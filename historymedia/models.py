from django.db import models
from user.models import User
# Create your models here.
class HistoryMedia(models.Model):
    id=models.AutoField(primary_key=True)
    id_media=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    type_media=models.IntegerField()
    day_watch=models.DateTimeField() 
    duration=models.CharField(max_length=200)
    def __str__(self):
        return self.id
    def set_day_watch(self,day_watch):
        self.day_watch = day_watch
    def set_duration(self,duration):
        self.duration = duration