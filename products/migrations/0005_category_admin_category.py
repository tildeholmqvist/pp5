# Generated by Django 4.2.11 on 2024-04-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_is_last_chance'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='admin_category',
            field=models.BooleanField(default=False),
        ),
    ]