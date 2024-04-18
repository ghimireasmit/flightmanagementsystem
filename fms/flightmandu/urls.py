from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('userhomepage/', views.userhomepage, name='userhomepage'),
    path('flightbooking/', views.flightbooking, name='flightbooking'),
    path('airlinelogin/', views.airlinelogin, name='airlinelogin'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
]