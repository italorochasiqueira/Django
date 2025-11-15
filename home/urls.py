#Arquivo criado para aninhar urls do App.
#Pode copiar o código do arquivo urls.py do project

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('exemplo/', views.exemplo1),
]
