# Generated by Django 4.2.5 on 2023-09-16 03:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0006_remove_cartitem_kids_name_remove_cartitem_parent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="active",
            field=models.BooleanField(default=True, verbose_name="active"),
        ),
    ]
