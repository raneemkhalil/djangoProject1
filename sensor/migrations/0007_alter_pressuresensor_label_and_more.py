# Generated by Django 4.1 on 2022-08-09 13:55

from django.db import migrations, models
import sensor.models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0006_alter_pressuresensor_pressuresensor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressuresensor',
            name='Label',
            field=models.CharField(max_length=70, validators=[sensor.models.mustStartWithPSSR]),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='PressureSensor_Id',
            field=models.CharField(auto_created=True, default='', max_length=50),
        ),
    ]