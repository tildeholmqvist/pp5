# Generated by Django 4.2.11 on 2024-04-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_price_product_large_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='large_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='medium_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='small_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='xlarge_price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=(60.00), max_digits=6),
            preserve_default=False,
        ),
    ]