# Generated by Django 4.1 on 2022-08-11 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choise_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choise',
            name='delete',
        ),
    ]
