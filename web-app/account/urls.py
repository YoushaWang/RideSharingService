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
    path('rider_view_request/',views.rider_view_request,name='rider_view_request'),
    path('<int:pk>/rider_edit_request',views.rider_edit_request,name='rider_edit_request'),
    path('<int:pk>/sharer_edit_request',views.sharer_edit_request,name='sharer_edit_request'),
    path('sharer_find_share_rides/',views.sharer_find_share_rides,name='sharer_find_share_rides'),
    path('sharer_join_ride/<int:pk>/<int:sharer_num>/',views.sharer_join_ride,name='sharer_join_ride'),
    # path('sharer_find_share_rides/',views.sharer_find_share_rides,name='sharer_find_share_rides/'),
    path('<int:pk>/order_detail',views.order_detail_pk,name='order_detail_pk'),
    path('<int:pk>/rider_order_detail',views.rider_order_detail_pk,name='rider_order_detail_pk'),
    path('<int:pk>/rider_order_details_car_info',views.rider_order_details_car_info_pk,name='rider_order_details_car_info_pk'),
    path('<int:pk>/order_detail_edit',views.order_detail_pk_edit,name='order_detail_pk_edit'),
]