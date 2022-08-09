import uuid

import rest_framework.status
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def mustStartWithPSSR(value):
    str = [*value]
    if str[0] != 'P' and str[1] != 'S' and str[2] != 'S' and str[3] != 'R':
        raise ValidationError('Value must start with PSSR', code=rest_framework.status.HTTP_400_BAD_REQUEST)


class PressureSensor(models.Model):

    Label = models.CharField(max_length=70, validators=[mustStartWithPSSR])
    InstallationDate = models.DateTimeField()
    Latitude = models.FloatField(default=100)
    Longitude = models.FloatField(default=100)
    PressureSensor_Id = models.CharField(max_length=50, null=False, default=uuid.uuid4)

    def __str__(self):
        return self.Label

class PressureReading(models.Model):

    SensorId = models.ForeignKey('PressureSensor', on_delete=models.CASCADE)
    DateTime = models.DateTimeField()
    Value = models.FloatField(default=0)

    # def __str__(self):
    #     return self.SensorId