# Generated by Django 4.2.5 on 2023-09-16 04:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_alter_generateqr_address_alter_generateqr_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generateqr",
            name="qr",
            field=models.ImageField(blank=True, upload_to="media"),
        ),
    ]
