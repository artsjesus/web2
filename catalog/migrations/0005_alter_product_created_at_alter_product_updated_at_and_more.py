# Generated by Django 5.1 on 2024-10-07 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=50, verbose_name='Номер версии')),
                ('version_name', models.CharField(max_length=150, verbose_name='Название версии')),
                ('is_current', models.BooleanField(default=False, verbose_name='Признак текущей версия')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
                'ordering': ['product'],
            },
        ),
    ]
