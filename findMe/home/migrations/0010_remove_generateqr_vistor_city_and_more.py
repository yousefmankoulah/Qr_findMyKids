# Generated by Django 4.2.5 on 2023-09-16 15:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_generateqr_vistor_city_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="generateqr",
            name="vistor_city",
        ),
        migrations.RemoveField(
            model_name="generateqr",
            name="vistor_country_name",
        ),
    ]
