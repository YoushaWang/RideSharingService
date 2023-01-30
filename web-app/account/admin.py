from django.contrib import admin
from .models import Account,Driver,Ride,UserDetail
# Register your models here.
admin.site.register(Account)
admin.site.register(Ride)
admin.site.register(Driver)
admin.site.register(UserDetail)
