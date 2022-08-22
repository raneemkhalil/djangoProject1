import datetime
import uuid

import django.utils.timezone
import rest_framework.status
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
from django.utils import timezone


def mustStartWithPSSR(value):
    str = [*value]
    if str[0] != 'P' and str[1] != 'S' and str[2] != 'S' and str[3] != 'R':
        raise ValidationError('Value must start with PSSR', code=rest_framework.status.HTTP_400_BAD_REQUEST)


class PressureSensor(models.Model):
    label = models.CharField(max_length=200, default='PSSR', validators=[mustStartWithPSSR])
    installation_date = models.DateField('date installation', default=datetime.date.today())
    latitude = models.DecimalField(
        max_digits=19, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=19, decimal_places=10, blank=True, null=True)
    serial_number = models.CharField(max_length=200, default=uuid.uuid4)

    def __str__(self):
        return self.label


class PressureReading(models.Model):
    sensor = models.ForeignKey(PressureSensor, related_name='readings', on_delete=models.CASCADE, default=1)
    date_time = models.DateTimeField('date installation', default=timezone.now())
    value = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)

    def __str__(self):
        return 'value={0} '.format(self.value)


class Stag(models.Model):
    pressure_sensor = models.ManyToManyField(PressureSensor, through='PressureSensorTag')
    label = models.CharField(max_length=200, default=" ")


class PressureSensorTag(models.Model):
    pressure_sensor = models.ForeignKey(PressureSensor, on_delete=models.CASCADE)
    stag = models.ForeignKey(Stag, on_delete=models.CASCADE)
