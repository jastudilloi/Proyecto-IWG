from django.contrib import admin
from django.urls import path, include
from apirkla import views as views1
from index import views as views2

urlpatterns = [
    path('index/', views2.landing),
    path('apirkla/valpo', views1.temp_valpo),
    path('apirkla/vina', views1.temp_viña),
]
