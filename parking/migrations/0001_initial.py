# Generated by Django 2.2.5 on 2019-10-12 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_number', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_number', models.CharField(max_length=2)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.Floor')),
            ],
        ),
    ]
