# Generated by Django 5.0.2 on 2024-05-03 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0012_rename_persons_carmodel_car_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placesmodel',
            name='location',
        ),
        migrations.DeleteModel(
            name='LocationModel',
        ),
    ]
