# Generated by Django 4.1 on 2022-08-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(blank=True, max_length=200, null=True)),
                ('vote', models.IntegerField(default=0)),
                ('delete', models.BooleanField(default=False)),
            ],
        ),
    ]