from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.PressureSensor)
class PressureSensor(admin.ModelAdmin):
    list_display = ('id', 'label', 'installation_date', 'latitude', 'longitude', 'serial_number')
    readonly_fields = ('serial_number',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.serial_number = request.user
        super().save_model(request, obj, form, change)

@admin.register(models.PressureReading)
class PressureReading(admin.ModelAdmin):
    list_display = ('id', 'date_time', 'value', 'sensor')