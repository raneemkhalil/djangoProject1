# Generated by Django 4.1 on 2022-08-24 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_questionchoice_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateField(default=datetime.date(2022, 8, 24)),
        ),
    ]
