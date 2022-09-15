import datetime

from django.core.exceptions import ObjectDoesNotExist
from django_filters.filterset import BaseFilterSet
from rest_framework import generics
from rest_framework import response
from rest_framework import viewsets, views
from .models import PressureSensor, PressureReading
from .serialize import PressureSensorSerializer, PressureReadingSerializer
from django_filters import rest_framework
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
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
    since = rest_framework.DateTimeFilter(field_name='date_time', lookup_expr='gte')
    until = rest_framework.DateTimeFilter(field_name='date_time', lookup_expr='lte')
    # DateTime = rest_framework.DateTimeFromToRangeFilter()

    class Meta:
        model = PressureReading
        fields = ['date_time']


class Sensors(viewsets.ViewSet):

    def list(self, request):
        queryset = PressureSensor.objects.all()
        serializer = PressureSensorSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request):
        PressureSensor.objects.get_or_create(label=request.POST.get('label'), installation_date=request.POST.get('InstallationDate'), longitude=request.POST.get('longitude'), latitude=request.POST.get('latitude'))
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

        dateTime = request.POST.get('date_time')
        dateTimeNu = datetime.datetime.fromisoformat(dateTime)

        try:
            sensorID = PressureSensor.objects.get(pk=request.POST.get('sensor_id')).pk
        except ObjectDoesNotExist:
            return response.Response({
                'data': [],
                'msg': 'The entire id is not exist!'
            })

        PressureReading.objects.get_or_create(sensor_id=sensorID, date_time=dateTimeNu, value=request.POST.get('value'))
        return response.Response({
            'data': [],
            'msg': 'Created!'
        })


class Calculating(views.APIView):

    def get(self, request):
        since = datetime.datetime.fromisoformat(request.GET.get('since'))
        until = datetime.datetime.fromisoformat(request.GET.get('until'))
        queryset = PressureReading.objects.filter(date_time__range=[since, until])

        if request.GET.get('calculation') == "sum":
            sum, count = summation(queryset)
            return response.Response(sum)
        elif request.GET.get('calculation') == "avg":
            sum, count = summation(queryset)
            avg = sum / count
            return HttpResponse(avg)
        else:
            return response.Response('please choice sum or avg')


def summation(queryset):
    sum = 0
    count = 0
    for obj in queryset:
        sum = sum + obj.value
        count = count + 1
    return sum, count


def calculating_readings(request):
    since = datetime.datetime.fromisoformat(request.GET.get('since'))
    until = datetime.datetime.fromisoformat(request.GET.get('until'))
    queryset = PressureReading.objects.filter(date_time__range=[since, until])

    if request.GET.get('calculation') == "sum":
        sum, count = summation(queryset)
        return HttpResponse(sum)
    elif request.GET.get('calculation') == "avg":
        sum, count = summation(queryset)
        avg = sum/count
        return HttpResponse(avg)
    else:
        return HttpResponse('please choice sum or avg')

