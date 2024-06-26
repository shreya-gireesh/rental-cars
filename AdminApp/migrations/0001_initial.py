# Generated by Django 5.0.2 on 2024-03-05 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=200)),
                ('admin_mail', models.CharField(max_length=200)),
                ('admin_pasw', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_name', models.CharField(max_length=200)),
                ('car_model', models.CharField(max_length=200)),
                ('car_year', models.DateField()),
                ('car_price', models.IntegerField()),
                ('status', models.CharField(default='Active', max_length=100)),
            ],
            options={
                'db_table': 'Car',
            },
        ),
    ]
