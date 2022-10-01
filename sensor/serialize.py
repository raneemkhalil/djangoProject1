from rest_framework import serializers
from .models import PressureSensor, PressureReading


class PressureSensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = PressureSensor
        fields = ['label', 'installation_date', 'latitude', 'longitude']


class PressureReadingSerializer(serializers.ModelSerializer):
    SensorId = PressureSensorSerializer(read_only=True)

    class Meta:
        model = PressureReading
        fields = ['SensorId', 'date_time', 'value', 'raw_value']
