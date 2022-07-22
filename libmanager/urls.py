from django.contrib import admin
from django.urls import path
from libmanager import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login', views.loginuser, name="login"),
    path('logout',views.logoutuser, name="logout"),
    path('addbook',views.addbook, name="addbook"),
    path('requestbook',views.requestbook, name="requestbook"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact")

]