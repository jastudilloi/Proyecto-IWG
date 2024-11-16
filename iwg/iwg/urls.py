from django.contrib import admin
from django.urls import path, include
from apirkla import views as views1
from index import views as views2

urlpatterns = [
    path('', views2.landing),
    path('consulta/valpo', views1.temp_valpo),
    path('consulta/vina', views1.temp_viña),
]
