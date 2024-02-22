from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminhomepage/', views.adminhomepage, name="adminhomepage"),
    path('airlinelogin/', views.airlinelogin, name="airlinelogin"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.signout, name="userlogout"),
]