# Generated by Django 4.2.6 on 2023-10-20 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0005_rename_about_hotelincity_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ThingsToKnow',
            new_name='Information',
        ),
    ]
