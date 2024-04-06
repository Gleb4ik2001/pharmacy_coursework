from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinLengthValidator,
    FileExtensionValidator,
    MinValueValidator
)
import os


class CompanyManufacturing(models.Model):
    title = models.CharField(
        verbose_name = 'название компании',
        unique=True,
        max_length = 150
    )

    def __str__(self) -> Any:
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'компания производитель'
        verbose_name_plural = 'компании производители'
        ordering = ('-id',)

class ShelfLife(models.Model):
    period = models.CharField(
        verbose_name = "период хранения препарата",
        max_length = 100,
        unique=True
    )

    def __str__(self):
        return self.period
    
    class Meta:
        verbose_name = 'срок хранения'
        verbose_name_plural = 'сроки хранения'
        ordering = ('-period',)

def product_image_upload(instance, filename):
    # Путь для загрузки файла: 'product_images/<название_препарата>/<имя_файла>'
    return os.path.join('product_images', instance.title, filename)

class Product(models.Model):
    title = models.CharField(
        verbose_name = 'название препарата',
        max_length = 150,
        unique = True,
        null = False
    )
    image = models.ImageField(
        verbose_name='фото препарата',
        upload_to=product_image_upload,
        null=  True,
        blank=True,
        default='product_images/scale_1200.png',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])
        ]
    )
    company_manufacturing = models.ForeignKey(
        verbose_name = 'компания производитель',
        to = CompanyManufacturing,
        null=False,
        blank = False,
        on_delete = models.PROTECT
    )
    composition = models.TextField(
        verbose_name = 'состав продукта',
        help_text=  'через запятую перечислите состав продукта',
    )
    shelf_life = models.ForeignKey(
        verbose_name = 'срок хранения препарата',
        to=ShelfLife,
        null=False,
        blank = False,
        on_delete = models.PROTECT
    )
    quantity = models.PositiveIntegerField(
        verbose_name = 'количество упаковок',
        validators = [
            MinValueValidator(0,message='количество не может быть отрицательным')
        ],
        default = 10
    )
    price = models.DecimalField(
        verbose_name  ='цена(KZT)',
        max_digits = 5,
        decimal_places = 2,
        default = 10
    )

    def __str__(self) -> str:
        return f'{self.title} | {self.price} KZT'
    
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('-title',)

