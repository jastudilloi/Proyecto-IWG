from django.urls import path
from . import views

urlpatterns = {
    path('obtener-temp/', views.sacartemp, name='sacartemp'),
}