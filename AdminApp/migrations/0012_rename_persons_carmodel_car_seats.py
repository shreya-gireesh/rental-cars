# Generated by Django 5.0.2 on 2024-04-09 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0011_carinteriorsmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='persons',
            new_name='car_seats',
        ),
    ]
