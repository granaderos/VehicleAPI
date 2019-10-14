# Generated by Django 2.2.6 on 2019-10-14 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_vehicleentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicleentry',
            old_name='vehicleStatus',
            new_name='vehicle_status',
        ),
        migrations.AlterField(
            model_name='vehicleentry',
            name='time_entry',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 14, 12, 7, 12, 905249)),
        ),
    ]