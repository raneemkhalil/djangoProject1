import datetime

from django.test import TestCase

from .models import PressureReading, PressureSensor
from . import views


since = datetime.datetime.fromisoformat('2022-01-01')
until = datetime.datetime.fromisoformat('2023-01-01')


class case1(TestCase):
    global since, until

    def test_queryset_equal(self):
        ps = PressureSensor.objects.create(label='PSSRfdgfh', installation_date='2022-04-22', latitude='101.5000000045',
                                           longitude='101.5000000548')
        PressureReading.objects.create(sensor=ps, date_time='2022-04-22 18:04:58+00', value=1.9000000000)
        PressureReading.objects.create(sensor=ps, date_time='2022-06-22 18:04:58+00', value=4.9000000000)
        queryset = PressureReading.objects.filter(date_time__range=[since, until])
        response, qs = views.math(since, until, 'sum')
        # self.assertQuerysetEqual(queryset, qs)

    def test_missing_parameter(self):
        response, q = views.math(None, until, 'sum')
        self.assertNotEqual(response, 'another params needed!')

    def test_until_after_since(self):
        self.assertNotEqual(views.math(since, until, 'sum'), 'since is grater than until pls switch')

    def test_retrieve_data_sum(self):

        ps = PressureSensor.objects.create(label='PSSRfdgfh', installation_date='2022-04-22', latitude='101.5000000045',
                                           longitude='101.5000000548')
        PressureReading.objects.create(sensor=ps, date_time='2022-04-22 18:04:58+00', value=1.9000000000)
        PressureReading.objects.create(sensor=ps, date_time='2022-06-22 18:04:58+00', value=4.9000000000)

        response, qs = views.math(since, until, 'sum')

        self.assertEqual(6.8, response)

        # client = Client()
        # url = reverse('calculate', {'since': '2022-01-01', 'until': '2023-01-01', 'calculation': 'sum'})
        # response = client.get(url)
        # print(response)

    def test_retrieve_data_avg(self):

        ps = PressureSensor.objects.create(label='PSSRfdgfh', installation_date='2022-04-22', latitude='101.5000000045',
                                           longitude='101.5000000548')
        PressureReading.objects.create(sensor=ps, date_time='2022-04-22 18:04:58+00', value=1.9000000000)
        PressureReading.objects.create(sensor=ps, date_time='2022-06-22 18:04:58+00', value=4.9000000000)

        response, qs = views.math(since, until, 'avg')

        self.assertEqual(3.4, response)

    def test_empty_queryset(self):
        ps = PressureSensor.objects.create(label='PSSRfdgfh', installation_date='2022-04-22', latitude='101.5000000045',
                                           longitude='101.5000000548')
        PressureReading.objects.create(sensor=ps, date_time='2022-04-22 18:04:58+00', value=1.9000000000)
        PressureReading.objects.create(sensor=ps, date_time='2022-06-22 18:04:58+00', value=4.9000000000)

        response, qs = views.math(since, until, 'avg')
        self.assertNotEqual(response, 0)

