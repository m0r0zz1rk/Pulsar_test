from django.core.validators import MinValueValidator
from django.db import models

from config.settings import MEDIA_ROOT
from products.images import WEBPImage

#Список возможных статусов товара
STATUSES_CHOICES = (
    ('В наличии', 'В наличии'),
    ('Под заказ', 'Под заказ'),
    ('Ожидается поступление', 'Ожидается поступление'),
    ('Нет в наличии', 'Нет в наличии'),
    ('Не производится', 'Не производится'),
)


def get_image_pass(instance, filename):
    """Путь сохранения изображения"""
    return f'{MEDIA_ROOT}/images/{instance.article}/{filename}'


class Products(models.Model):
    """Модель продуктов"""
    name = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    article = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Артикул'
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0), ],
        blank=False,
        null=False,
        verbose_name='Цена'
    )
    status = models.CharField(
        max_length=50,
        choices=STATUSES_CHOICES,
        blank=False,
        null=False,
        verbose_name='Статус'
    )
    image = WEBPImage(
        upload_to=get_image_pass,
        verbose_name='Изображение'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.name} ({self.article})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'