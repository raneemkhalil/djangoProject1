# Generated by Django 4.1 on 2022-08-19 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_choise_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateField(default=datetime.date(2022, 8, 19)),
        ),
    ]
