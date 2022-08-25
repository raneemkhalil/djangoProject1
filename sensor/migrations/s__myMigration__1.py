from django.db import migrations


def code(apps, schema_editor):
    pressure_readings = apps.get_model('sensor', 'PressureReading')
    db_alias = schema_editor.connection.alias
    values = pressure_readings.objects.all()
    for value in values:
        value.raw_value = value.value

    pressure_readings.objects.using(db_alias).bulk_update(values, ['raw_value'])


def reverse_code(apps, schema_editor):
    pressure_readings = apps.get_model('sensor', 'PressureReading')
    db_alias = schema_editor.connection.alias
    queryset = pressure_readings.objects.all()
    for obj in queryset:
        obj.raw_value = ' '
    pressure_readings.objects.using(db_alias).bulk_update(queryset, ['raw_value'])


class Migration(migrations.Migration):
    dependencies = [('sensor', '0004_alter_pressurereading_date_time')]
    operations = [
        migrations.RunPython(code, reverse_code),
    ]
