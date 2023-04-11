from django.db import models

# Create your models here.
class User(models.Model):
    id_user=models.AutoField(primary_key=True,)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    full_name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    gender=models.CharField(max_length=200,null=True)
    role=models.CharField(max_length=200,default="member")
    is_vip=models.CharField(max_length=10,default="0")
    def __str__(self):
        return self.id_user
    def set_role(self, role):
        self.role = role
    def set_is_vip(self, is_vip):
        self.is_vip=is_vip
    def set_id(self,id):
        self.id_user =id
    def set_fullname(self,fullname):
        self.full_name=fullname
    def set_address(self,address):
        self.address=address
    def set_phone(self,phone):
        self.phone=phone
    def set_gender(self,gender):
        self.gender=gender
    def set_role(self,role):
        self.role=role