from django.urls import path

from . import views

urlpatterns = [
    path('api/pressure_sensors/', views.Sensors.as_view({'get': 'list', 'post': 'create'}), name='pressure_sensors'),
    path('api/pressure_readings/', views.Readings.as_view({'get': 'list', 'post': 'create'})),
]