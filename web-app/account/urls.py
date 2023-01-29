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
]