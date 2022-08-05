from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.PressureSensor)
class PressureSensor(admin.ModelAdmin):
    list_display = ('id', 'Label', 'InstallationDate', 'Latitude', 'Longitude')

@admin.register(models.PressureReading)
class PressureReading(admin.ModelAdmin):
    list_display = ('id', 'DateTime', 'Value', 'SensorId')