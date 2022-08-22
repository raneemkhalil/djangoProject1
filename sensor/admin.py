from django.contrib import admin
from django.contrib.contenttypes import admin as ad
from . import models
from fl_tags import models as md
# Register your models here.


class Tags(ad.GenericTabularInline):
    model = md.Tag
    fields = ['tag']
    extra = 1  # in my model always shows a 1 empty field.


class PressureSensorTags(admin.TabularInline):
    model = models.PressureSensorTag
    extra = 1


class PressureSensor(admin.ModelAdmin):
    list_display = ('id', 'label', 'installation_date', 'latitude', 'longitude', 'serial_number')
    readonly_fields = ('serial_number',)
    inlines = [PressureSensorTags]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.serial_number = request.user
        super().save_model(request, obj, form, change)


class PressureReading(admin.ModelAdmin):
    list_display = ('id', 'date_time', 'value', 'sensor')
    inlines = [Tags]


class Stags(admin.ModelAdmin):
    list_display = ('pressure_sensor', 'label')


admin.site.register(models.PressureSensor, PressureSensor)

admin.site.register(models.PressureReading, PressureReading)

admin.site.register(models.Stag)

admin.site.register(models.PressureSensorTag)

# admin.site.register(md.Tag) : one statement is enough
