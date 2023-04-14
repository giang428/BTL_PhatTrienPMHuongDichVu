from django.db import models
from user.models import User
# Create your models here.

class MediaReaction(models.Model):
    id_mreaction=models.AutoField(primary_key=True)
    id_media=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    day_reaction=models.DateField()
    type_media=models.IntegerField()
    type_reaction=models.IntegerField()
    type_favorite=models.IntegerField()
    def __str__(self):
        return self.id_mreaction
    def set_type_reaction(self,type_reaction):
        self.type_reaction = type_reaction
    def set_type_favorite(self,type_favorite):
        self.type_favorite = type_favorite
