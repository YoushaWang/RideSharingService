from django.contrib import admin
from .models import Account,Driver
from .models import RideRequest
# Register your models here.
admin.site.register(Account)
admin.site.register(Driver)
admin.site.register(RideRequest)