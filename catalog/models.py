from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    # created_at = models.TextField(verbose_name='создание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='наименование')
    price = models.IntegerField(**NULLABLE, verbose_name='цена за штуку')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='фото')
    date_create = models.DateField(**NULLABLE, auto_now_add=True, verbose_name='дата создания')
    date_change = models.DateField(**NULLABLE, auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
