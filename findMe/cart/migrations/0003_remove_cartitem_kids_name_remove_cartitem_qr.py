# Generated by Django 4.2.5 on 2023-09-12 19:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0002_cartitem_kids_name_cartitem_qr"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="kids_name",
        ),
        migrations.RemoveField(
            model_name="cartitem",
            name="qr",
        ),
    ]
