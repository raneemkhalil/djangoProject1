from django.db import models

# Create your models here.
class PressureSensor(models.Model):

    Label = models.CharField(max_length=70)
    InstallationDate = models.DateTimeField()
    Latitude = models.FloatField(default=100)
    Longitude = models.FloatField(default=100)

    def __str__(self):
        return self.Label

class PressureReading(models.Model):

    SensorId = models.ForeignKey('PressureSensor', on_delete=models.CASCADE)
    DateTime = models.DateTimeField()
    Value = models.FloatField(default=0)

    def __str__(self):
        return self.SensorId