# Generated by Django 2.2.6 on 2019-10-14 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_auto_20191014_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicleentry',
            name='vehicle_status',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('CLEARED', 'Cleared'), ('UNREGISTERED', 'Unregistered'), ('CARNAPPED', 'Carnapped'), ('DUPLICATE', 'Duplicate'), ('CODING', 'Coding Violation')], default='CLEARED', max_length=64),
        ),
        migrations.AlterField(
            model_name='vehicleentry',
            name='time_entry',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 14, 13, 56, 38, 566834)),
        ),
        migrations.DeleteModel(
            name='VehicleStatus',
        ),
    ]
