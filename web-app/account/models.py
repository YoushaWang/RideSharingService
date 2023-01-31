from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model
# User = get_user_model
from django.contrib.auth.models import User
from phone_field import PhoneField
#note:
# if want to change the existed model,
# should detete the data in database first
# Create your models here.
TYPE_CHOICES=(
    ("NONE","NONE"),
    ("SUV", "SUV"),
    ("COMPACT", "COMPACT"),
    ("COMFORT", "COMFORT"),
    ("GREEN", "GREEN"),
    ("PREMIER","PREMIER"),
)
STATUS=(
    ("OPEN","OPEN"),
    ("COMFIRM","COMFIRM"),
    ("COMPLETE","COMPLETE"),
)
# class UserDetail(models.Model):


class Account(models.Model):
    user_name = models.OneToOneField(User, on_delete = models.CASCADE,default="")
    email=models.EmailField(max_length = 100,null=True,blank=True)
#     tel=models.CharField(max_length=18,null=True,blank=True)
#     first_name = models.CharField(max_length=100,null=True,blank=True)
#     last_name = models.CharField(max_length=100,null=True,blank=True)
#     password=models.CharField(max_length=20,null=True,blank=True)
#     drive=models.BooleanField(default=False,blank=True)
#     license_num=models.CharField(max_length=20,null=True,blank=True)
#     license_plate=models.CharField(max_length=20,null=True,blank=True)
#     car_type=models.CharField(max_length = 20, choices = TYPE_CHOICES, default = 'SUV',null=True,blank=True)
#     # insurance=models.CharField(max_length=20,null=True)
#     car_brand=models.CharField(max_length=20,null=True,blank=True)
#     capacity=models.PositiveIntegerField(default=1,null=True,blank=True)
#     # username = models.OneToOneField(User,on_delete=models.CASCADE)  
#     # identity = models.BooleanField(default=True)#models.BooleanField(help_text="Are you driver?")
    
    def __str__(self):
        return self.user_name

class Ride(models.Model):
#     #people
    #basic info
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    rider_num=models.PositiveIntegerField(default=1)
    capacity=models.PositiveIntegerField(default=1)
    #added info
    driver = models.CharField(max_length=20,null=True,default="")
    #share info
    ifShare=models.BooleanField(default=False)
    sharer = models.CharField(max_length=20,null=True,default="")
    sharer_num=models.PositiveIntegerField(default=0)
    #place & time & info
    pickup=models.CharField(max_length=100,default="NONE")
    whereto=models.CharField(max_length=100,default="NONE")
    schedule=models.DateTimeField(auto_now_add=True)
    extraInfo=models.CharField(max_length=200,default="NONE")
    car_type=models.CharField(max_length = 20, choices = TYPE_CHOICES, default = 'SUV')
    #status
    status=models.CharField(max_length = 20, choices = STATUS, default = 'OPEN')
    def __str__(self):
        return self.owner.username
    


# #useless
class Driver(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    license_num=models.CharField(max_length=20,default = '',blank=True)

class UserDetail(models.Model):
    username = models.OneToOneField(User, on_delete = models.CASCADE,default="")
    email=models.EmailField(max_length = 100,null=True,blank=True)
    tel=models.CharField(max_length=18,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
    drive=models.BooleanField(default=False,blank=True)
    license_num=models.CharField(max_length=20,null=True,blank=True)
    license_plate=models.CharField(max_length=20,null=True,blank=True)
    car_type=models.CharField(max_length = 20, choices = TYPE_CHOICES, default = "NONE",null=True,blank=True)
    car_brand=models.CharField(max_length=20,null=True,blank=True)
    capacity=models.PositiveIntegerField(default=1,null=True,blank=True)
    def __str__(self):
        return self.username.username
