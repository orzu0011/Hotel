# Generated by Django 3.2.12 on 2023-10-27 13:24

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiences_descriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144)),
                ('descriptions1', models.CharField(max_length=150)),
                ('descriptions2', models.CharField(max_length=150)),
                ('descriptions3', models.CharField(max_length=150)),
                ('descriptions4', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Experiences_descriptions',
                'verbose_name_plural': 'Experiences_descriptionss',
            },
        ),
        migrations.CreateModel(
            name='Experiences_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('person_cost', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
            ],
            options={
                'verbose_name': 'Experiences_list',
                'verbose_name_plural': 'Experiences_lists',
            },
        ),
        migrations.CreateModel(
            name='Include',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('include', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Include',
                'verbose_name_plural': 'Includes',
            },
        ),
        migrations.CreateModel(
            name='Things_to_know',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144)),
                ('descriptions1', models.CharField(max_length=150)),
                ('descriptions2', models.CharField(max_length=150)),
                ('descriptions3', models.CharField(max_length=150)),
                ('descriptions4', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ExperiencesCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_check_in', models.DateField(default=datetime.datetime.now)),
                ('person_check_out', models.DateField(default=datetime.datetime.now)),
                ('guests', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('guests_main', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('service_charge', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('Adults', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('Children', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('Infants', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)])),
                ('person_price_per_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.experiences_list')),
            ],
            options={
                'verbose_name': 'HotelInCityCost',
                'verbose_name_plural': 'HotelInCityCosts',
            },
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('hour', models.TimeField()),
                ('number_of_people', models.SmallIntegerField()),
                ('language', models.CharField(max_length=144)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='img')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.experiences_list')),
            ],
            options={
                'verbose_name': 'Experiences',
                'verbose_name_plural': 'Experiencess',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.experiences')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
