# Generated by Django 4.2.5 on 2023-09-12 00:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_generateqr_qr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generateqr",
            name="qr",
            field=models.ImageField(blank=True, upload_to="media/qr/"),
        ),
    ]
