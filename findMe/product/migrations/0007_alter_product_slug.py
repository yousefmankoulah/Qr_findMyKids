# Generated by Django 4.2.5 on 2023-09-16 04:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_alter_category_description_alter_category_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
