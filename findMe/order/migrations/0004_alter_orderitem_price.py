# Generated by Django 4.2.5 on 2023-09-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_orderitem_kids_name_orderitem_parent_orderitem_qr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Price"
            ),
        ),
    ]