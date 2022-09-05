import datetime

import requests
from django.test import TestCase, Client
from django.urls import reverse, resolve
# from .views import calculating_readings
# Create your tests here.
from .models import PressureReading, PressureSensor
from . import views

# class ParamsTestCase1(TestCase):
#
#     def test_calculate_params(self):
#         client = Client()
#         # url = reverse('fun_calculate')
#         responce = client.get('api/fun_calculate', {'since': ' ', 'until': ' ', 'calculation': ' '})
#         print(responce.path)
#         # self.assertEqual(responce.GET, 'since')
#         # print(resolve(url).func)

# class ParamsTestCase2(TestCase):
#
#     def test_calculation_params1(self):
#         pass
#         # request = RequestFactory().get('api/fun_calculate/')
#         # view = calculating_readings(request)
#         # view.setup(request)
#         # context = view.get_context_data()
#         # self.assertIn('until', context, 'not contain')


class case1(TestCase):

    def test_retrieve_data(self):
        sum = avg = count = 0
        since = datetime.datetime.fromisoformat('2022-01-01')
        until = datetime.datetime.fromisoformat('2023-01-01')

        ps = PressureSensor.objects.create(label='PSSRfdgfh', installation_date='2022-04-22', latitude='101.5000000045',
                                           longitude='101.5000000548')
        PressureReading.objects.create(sensor=ps, date_time='2022-04-22 18:04:58+00', value=1.9000000000)
        PressureReading.objects.create(sensor=ps, date_time='2022-06-22 18:04:58+00', value=4.9000000000)

        self.assertFalse(views.missing_param(since, until, 'sum'))
        self.assertFalse(views.is_greater(since, until))

        queryset = PressureReading.objects.filter(date_time__range=[since, until])

        for obj in queryset:
            sum = sum + obj.value
            count = count + 1

        avg = sum/count

        response, qs = views.math(since, until, 'sum')
        response1, qs1 = views.math(since, until, 'avg')

        # self.assertQuerysetEqual(queryset, qs)
        self.assertEqual(sum, response)
        self.assertEqual(avg, response1)
        self.assertNotEqual(response, 0)

        # client = Client()
        # url = reverse('calculate', {'since': '2022-01-01', 'until': '2023-01-01', 'calculation': 'sum'})
        # response = client.get(url)
        # print(response)

