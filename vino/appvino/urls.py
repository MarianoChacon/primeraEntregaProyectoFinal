from django.contrib import admin
from django.urls import path
from appvino import views

urlpatterns = [
    path('', views.inicio),
    path('ususarios', views.usuarios),
    path('bodegas', views.bodegas),
    path('vinos', views.vinos),
]