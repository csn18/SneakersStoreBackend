from django.db import models
from django.contrib.auth.models import User


class Sizes(models.Model):
    """ Размеры """
    size = models.PositiveIntegerField(verbose_name='Размер')

    def __str__(self):
        return f'{self.size}'


class Brand(models.Model):
    """ Названия брендов """
    brand_name = models.CharField(verbose_name='Название бренда', max_length=255)

    def __str__(self):
        return f'{self.brand_name}'


class ShopItem(models.Model):
    """ Товар """
    title = models.CharField(verbose_name='Название товара', max_length=255)
    description = models.TextField(verbose_name='Описание', max_length=4096)
    price = models.DecimalField(verbose_name='Стоимость', decimal_places=2, max_digits=12)
    brand = models.ForeignKey(verbose_name='Бренд', to=Brand, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(verbose_name='Размеры', to=Sizes)

    def __str__(self):
        return f'{self.title}'


class ItemImage(models.Model):
    """ Фотографии товара """
    item = models.ForeignKey(verbose_name='', to=ShopItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Фотография', upload_to='image')


class Cart(models.Model):
    """ Корзина товаров """
    owner = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE, related_name='owner_cart')
    shop_items = models.ManyToManyField(verbose_name='Продукт', to=ShopItem)

    def __str__(self):
        return f'Корзина {self.owner}'
