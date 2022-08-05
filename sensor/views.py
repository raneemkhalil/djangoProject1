import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework import response
from rest_framework import viewsets
from .models import PressureSensor, PressureReading
from .serialize import PressureSensorSerializer, PressureReadingSerializer
from django_filters import rest_framework
# Create your views here.

# class Sensors(generics.ListAPIView):
#     queryset = PressureSensor.objects.all()
#     serializer_class = PressureSensorSerializer
#
#
# class Reading(generics.ListAPIView):
#     queryset = PressureReading.objects.all()
#     serializer_class = PressureReadingSerializer
#
#     def get_queryset(self):
#         date1 = datetime.datetime.fromisoformat(self.request.GET['from'])
#         date2 = datetime.datetime.fromisoformat(self.request.GET['to'])
#         pressure_readings = PressureReading.objects.filter(DateTime__range=[date1, date2]).select_related()
#         return pressure_readings


class ReadingsFilter(rest_framework.FilterSet):
    # from_date = rest_framework.DateTimeFilter(field_name='DateTime', lookup_expr='gte')
    # to_date = rest_framework.DateTimeFilter(field_name='DateTime', lookup_expr='lte')
    DateTime = rest_framework.DateTimeFromToRangeFilter()

    class Meta:
        model = PressureReading
        fields = ['DateTime']


class Sensors(viewsets.ViewSet):

    def list(self, request):
        queryset = PressureSensor.objects.all()
        serializer = PressureSensorSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request):
        PressureSensor.objects.get_or_create(Label=request.POST.get('label'), InstallationDate=request.POST.get('InstallationDate'), Longitude=request.POST.get('longitude'), Latitude=request.POST.get('latitude'))
        return response.Response({
            'data': [],
            'msg': 'Created!'
        })


class Readings(viewsets.ModelViewSet):

    queryset = PressureReading.objects.all().values()
    serializer_class = PressureReadingSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = ReadingsFilter
    # filterset_fields = ('Value',)

    def list(self, request, *args, **kwargs):
        return response.Response(self.filter_queryset(self.queryset))

    def create(self, request, *args, **kwargs):

        dateTime = request.POST.get('DateTime')
        dateTimeNu = datetime.datetime.fromisoformat(dateTime)

        try:
            sensorID = PressureSensor.objects.get(pk=request.POST.get('sensorID'))
        except ObjectDoesNotExist:
            return response.Response({
                'data': [],
                'msg': 'The entire id is not exist!'
            })

        PressureReading.objects.get_or_create(SensorId=sensorID, DateTime=dateTimeNu, Value=request.POST.get('value'))
        return response.Response({
            'data': [],
            'msg': 'Created!'
        })