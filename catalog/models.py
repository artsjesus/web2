from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to="catalog/image", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория", blank=True, null=True, related_name="Products")
    price = models.FloatField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(verbose_name="Дата создания")
    updated_at = models.DateTimeField(verbose_name="Дата последнего изменения")
    manufactured_at = models.DateTimeField(verbose_name="Дата производства продукта", blank=True, null=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", ["name"]]

    def __str__(self):
        return self.name
