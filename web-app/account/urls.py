from django.urls import path
# from catalog import views
# urlpatterns = [
# ]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='loginPage'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('main/',views.main,name='main'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('terms_and_conditions/',views.terms_and_conditions,name='terms_and_conditions'),
    path('driver_open_ride/',views.driver_open_ride,name='driver_open_ride'),
    path('driver_confirmed_ride/',views.driver_confirmed_ride,name='driver_confirmed_ride'),
    path('rider_request_ride/',views.rider_request_ride,name='rider_request_ride'),
    path('order_detail/',views.order_detail,name='order_detail'),
]