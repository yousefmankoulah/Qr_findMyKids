# Generated by Django 4.2.5 on 2023-09-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_generateqr_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generateqr",
            name="type",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
