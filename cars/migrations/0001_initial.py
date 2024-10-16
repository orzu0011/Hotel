# Generated by Django 3.2.12 on 2023-10-30 14:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_owner', models.CharField(max_length=255, verbose_name='Mashina oluvchi shaxs')),
                ('seats', models.IntegerField(default=0, verbose_name='O`rindiqlar soni')),
                ('bags', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
            options={
                'verbose_name': 'Mashina',
                'verbose_name_plural': 'Mashinalar',
            },
        ),
        migrations.CreateModel(
            name='Car_description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Izoh')),
            ],
            options={
                'verbose_name': "Mashina ha1qida ma'lumot",
                'verbose_name_plural': "Mashina ha1qida ma'lumotlar",
            },
        ),
        migrations.CreateModel(
            name='CarAdvantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_consumption', models.CharField(max_length=150)),
                ('electric_combined', models.IntegerField()),
                ('touchscreen_display', models.IntegerField()),
                ('light', models.CharField(max_length=50)),
                ('forward_collision', models.CharField(max_length=222)),
                ('fire', models.CharField(max_length=121)),
                ('stop_and_go', models.CharField(max_length=222)),
                ('b_c_w', models.CharField(max_length=222)),
            ],
            options={
                'verbose_name': 'Mashina afzalligi',
                'verbose_name_plural': 'Mashina afzalliklari',
            },
        ),
        migrations.CreateModel(
            name='CarInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222, verbose_name='Sarlavha')),
                ('cancellation_policy_title', models.CharField(max_length=121, verbose_name="Bekor qilish ko'rsatmasi")),
                ('cancellation_policy_description', models.TextField(verbose_name="Bekor qilish ko'rsatmasi izohi")),
                ('special_note_title', models.CharField(max_length=100, verbose_name='Maxsus qayd')),
                ('special_note_description', models.TextField(verbose_name='Maxsus qayd izohi')),
            ],
            options={
                'verbose_name': "Bilish kerak bo'lgan narsalar",
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_name', models.CharField(max_length=255, verbose_name='Mashina nomi')),
                ('seats', models.IntegerField(default=0)),
                ('choice', models.CharField(choices=[('mehanika', 'mexanika'), ('auto gearbox', 'avtomat karobka')], max_length=100, verbose_name='Ishlash usuli')),
                ('price_days', models.IntegerField(default=0, verbose_name="kunlik to'lov")),
                ('picture', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
            options={
                'verbose_name': "Mashina ro'yxati",
                'verbose_name_plural': "Mashinalar ro'yxati",
            },
        ),
        migrations.CreateModel(
            name='CoolModelBro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limited_integer_field', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Include',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence1', models.CharField(max_length=500, null=True)),
                ('sentence2', models.CharField(max_length=500, null=True)),
                ('sentence3', models.CharField(max_length=500, null=True)),
                ('sentence4', models.CharField(max_length=500, null=True)),
                ('sentence5', models.CharField(max_length=500, null=True)),
                ('sentence6', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('description', models.TextField(verbose_name='Izoh')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
            options={
                'verbose_name': 'komment',
                'verbose_name_plural': 'kommentlar',
            },
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Ismi')),
                ('places', models.SmallIntegerField()),
                ('description', models.TextField(verbose_name='Izoh')),
                ('joined', models.CharField(max_length=255)),
                ('response_time', models.CharField(max_length=100)),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.coolmodelbro')),
            ],
            options={
                'verbose_name': 'Mashina oluvshi shaxs',
                'verbose_name_plural': 'Mashina oluvshi shaxslar',
            },
        ),
        migrations.CreateModel(
            name='CarCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('car_pick_up', models.DateField(auto_now_add=True)),
                ('car_drop_off', models.DateField(auto_now_add=True)),
                ('car_price_per_day', models.IntegerField(blank=True, default=0, null=True)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(0)])),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.cars', verbose_name='Mashina nomi'),
        ),
    ]
