from django.urls import path

from . import views
from django.http import request

urlpatterns = [
    path('api/pressure_sensors/', views.Sensors.as_view({'get': 'list', 'post': 'create'}), name='pressure_sensors'),
    path('api/pressure_readings/', views.Readings.as_view({'get': 'list', 'post': 'create'})),
    path('api/fun_calculate/', views.calculating_readings, name='calculate'),
    path('api/class_calculate/', views.Calculating.as_view(), name='calculation'),
    path('api/greet/', views.greet_users, name='greeting'),
]
