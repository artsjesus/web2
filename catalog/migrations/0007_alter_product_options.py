# Generated by Django 4.2.2 on 2024-10-20 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'name'], 'permissions': [('can_edit_description', 'can edit description'), ('can_edit_category', 'can edit category'), ('can_unpublish', 'can unpublish')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
