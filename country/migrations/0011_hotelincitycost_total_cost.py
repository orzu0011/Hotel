# Generated by Django 4.2.6 on 2023-10-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0010_hotelincitycost_alter_author_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelincitycost',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=18),
            preserve_default=False,
        ),
    ]
