from django.contrib import admin
from django.urls import path, include
from apirkla import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apirkla/valpo', views.temp_valpo),
    path('apirkla/vina', views.temp_viña),
]
