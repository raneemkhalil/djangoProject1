import datetime

import requests
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import response, views, viewsets, status
from rest_framework.decorators import api_view
from .models import PressureSensor, PressureReading
from .serialize import PressureSensorSerializer, PressureReadingSerializer
from django_filters import rest_framework
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from django.shortcuts import redirect

log = logging.getLogger('__name__')
# Create your views here.

# class Sensors(generics.ListAPIView):
#     queryset = PressureSensor.objects.all()
#     serializer_class = PressureSensorSerializer


# class Reading(generics.ListAPIView):
#     queryset = PressureReading.objects.all()
#     serializer_class = PressureReadingSerializer
#
#     def get_queryset(self):
#         date1 = datetime.datetime.fromisoformat(self.request.GET['from'])
#         date2 = datetime.datetime.fromisoformat(self.request.GET['to'])
#         pressure_readings = PressureReading.objects.filter(DateTime__range=[date1, date2]).select_related()
#         return pressure_readings

############# a functions to be test ###############

def is_greater(x, y):
    if x > y:
        return True
    else:
        return False


def math(since, until, operation):

    if missing_param(since, until, operation):
        return 'another params needed!', []

    if is_greater(since, until):
        return 'since is grater than until pls switch', []

    queryset = PressureReading.objects.filter(date_time__range=[since, until])

    if queryset.count() == 0:
        return 0, queryset

    sum, count = summation(queryset)

    if operation == "sum":
        return sum, queryset
    elif operation == "avg":
        avg = sum/count
        return avg, queryset
    else:
        return 'please choice sum or avg', queryset


def missing_param(since, until, calculation):
    if since is None or until is None or calculation is None:
        return True


class ReadingsFilter(rest_framework.FilterSet):
    # since = rest_framework.DateTimeFilter(field_name='date_time', lookup_expr='gte')
    # until = rest_framework.DateTimeFilter(field_name='date_time', lookup_expr='lte')
    DateTime = rest_framework.DateTimeFromToRangeFilter()

    class Meta:
        model = PressureReading
        fields = ['date_time']


class Sensors(viewsets.ModelViewSet):
    queryset = PressureSensor.objects.all()
    serializer_class = PressureSensorSerializer

    def list(self, request, *args, **kwargs):
        serializer = PressureSensorSerializer(self.queryset, many=True)
        return response.Response(serializer.data)

    def create(self, request, *args, **kwargs):
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


def summation(queryset):
    sum = 0
    count = 0
    for obj in queryset:
        sum = sum + obj.value
        count = count + 1
    return sum, count


class Calculating(views.APIView):

    def get(self, request):

        since = datetime.datetime.fromisoformat(request.GET.get('since'))
        until = datetime.datetime.fromisoformat(request.GET.get('until'))
        operation = request.GET.get('calculation')
        if missing_param(since, until, operation):
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        result, qs = math(since, until, operation)
        return response.Response(result)


def calculating_readings(request):

    since = datetime.datetime.fromisoformat(request.GET.get('since'))
    until = datetime.datetime.fromisoformat(request.GET.get('until'))
    operation = request.GET.get('calculation')
    result, qs = math(since, until, operation)
    return response.Response(result)


@csrf_exempt
@api_view(['POST', 'GET'])
@login_required(login_url='/admin/login/')
def greet_users(request):
    if request.method == "POST" and 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return HttpResponse('Hello ' + request.user.username + '!')
            # if not request.user.is_authenticated:
            #     return redirect('%s?next=%s' % ('/admin/login/', '/api/greet/'))
        else:
            return HttpResponse('invalid input!')
    else:
        return HttpResponse('Hello ' + request.user.username + '!')
        # if request.user.is_authenticated:
        #     return HttpResponse('Hello ' + request.user.username + '!')
        # else:
        #     return redirect('%s?next=%s' % ('/admin/login/', '/api/greet/'))
