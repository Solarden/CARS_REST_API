# Generated by Django 3.2.10 on 2021-12-28 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_api', '0004_auto_20211228_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='rates_number',
        ),
    ]
