# Generated by Django 4.1 on 2022-08-09 14:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0007_alter_pressuresensor_label_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressuresensor',
            name='PressureSensor_Id',
            field=models.CharField(default=uuid.uuid4, max_length=50),
        ),
    ]
