# Generated by Django 5.0.2 on 2024-04-07 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0011_carinteriorsmodel'),
        ('UserApp', '0005_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.bookingmodel'),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.carmodel'),
        ),
    ]
