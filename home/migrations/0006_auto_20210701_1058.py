# Generated by Django 2.2.14 on 2021-07-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
