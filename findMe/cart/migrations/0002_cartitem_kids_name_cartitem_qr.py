# Generated by Django 4.2.5 on 2023-09-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="kids_name",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="qr",
            field=models.ImageField(blank=True, upload_to="media"),
        ),
    ]