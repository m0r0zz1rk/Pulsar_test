# Generated by Django 4.1.4 on 2022-12-13 11:26

from django.db import migrations, models
import products.images
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=products.images.WEBPImage(upload_to=products.models.get_image_pass, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('В наличии', 'В наличии'), ('Под заказ', 'Под заказ'), ('Ожидается поступление', 'Ожидается поступление'), ('Нет в наличии', 'Нет в наличии'), ('Не производится', 'Не производится')], max_length=50, verbose_name='Статус'),
        ),
    ]
