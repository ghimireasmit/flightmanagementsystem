from django.contrib import admin
from django.urls import path, include
from . import views
from .views import check_email_availability, check_phone_availability

urlpatterns = [
    path('', views.index, name='home'),
    path('check_email_availability/', check_email_availability, name='check_email_availability'),
    path('check_phone_availability/', check_phone_availability, name='check_phone_availability'),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('userhomepage/', views.userhomepage, name='userhomepage'),
    path('flightbooking/', views.flightbooking, name='flightbooking'),
    path('contactus/', views.contactus, name='contactus'),
]