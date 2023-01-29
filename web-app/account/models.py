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
    ("SUV", "SUV"),
    ("COMPACT", "COMPACT"),
    ("COMFORT", "COMFORT"),
    ("GREEN", "GREEN"),
    ("PREMIER","PREMIER"),
)
class Account(models.Model):
    # userid=models.CharField(max_length=5,null=True)
    username = models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length = 100,null=True)
    tel=PhoneField(blank=True, help_text='Contact phone number')
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=20,null=True)
    drive=models.BooleanField(default=False)
    license_num=models.CharField(max_length=20,null=True)
    license_plate=models.CharField(max_length=20,null=True)
    car_type=models.CharField(max_length = 20, choices = TYPE_CHOICES, default = 'SUV')
    # insurance=models.CharField(max_length=20,null=True)
    car_brand=models.CharField(max_length=20,null=True)
    # seat_num=models.CharField(max_length=20,null=True)
    capacity=models.PositiveIntegerField(default=0)
    # username = models.OneToOneField(User,on_delete=models.CASCADE)  
    # identity = models.BooleanField(default=True)#models.BooleanField(help_text="Are you driver?")
    
    def __str__(self):
        return self.username

class Driver(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    license_num=models.CharField(max_length=20,default = '',blank=True)
