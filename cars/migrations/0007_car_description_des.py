# Generated by Django 4.2.6 on 2023-11-01 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_caradvantages_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_description',
            name='des',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
            preserve_default=False,
        ),
    ]
