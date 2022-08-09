from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.PressureSensor)
class PressureSensor(admin.ModelAdmin):
    list_display = ('id', 'Label', 'InstallationDate', 'Latitude', 'Longitude', 'PressureSensor_Id')
    readonly_fields = ('PressureSensor_Id',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.PressureSensor_Id = request.user
        super().save_model(request, obj, form, change)

@admin.register(models.PressureReading)
class PressureReading(admin.ModelAdmin):
    list_display = ('id', 'DateTime', 'Value', 'SensorId')