# Generated by Django 5.1 on 2024-09-05 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_date_create_product_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата производства продукта'),
        ),
    ]
