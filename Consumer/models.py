from django.contrib.auth.models import AbstractUser
from django.db import models

from Auth.manager import CustomUserManager
from Auth.models import User
from Seller.models import ProductItem


class Geolocate(models.Model):
    """ Геолокация """
    latitude = models.CharField('Широта', max_length=255, blank=True)
    longitude = models.CharField('Долгота', max_length=255, blank=True)

    def __str__(self):
        return f'Широта {self.latitude} Долгота {self.latitude}'

    class Meta:
        verbose_name = 'Геолокация'
        verbose_name_plural = 'Геолокации'


class Address(models.Model):
    """ Адрес доставки """
    region = models.CharField('Регион', max_length=255, blank=True)
    city = models.CharField('Город', max_length=255, blank=True)
    street = models.CharField('Улица', max_length=255, blank=True)
    home = models.PositiveIntegerField('Номер дома', blank=True)
    flat = models.PositiveIntegerField('Номер квартиры', blank=True)

    def __str__(self):
        return f'Адрес доставки {self.id}'

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адреса доставки'


class Consumer(User):
    """ Покупатель """
    phone = models.CharField('Телефон', max_length=11, blank=True, null=True)
    address = models.ForeignKey(
        Address, on_delete=models.PROTECT, blank=True, null=True)
    geolocate = models.ForeignKey(
        Geolocate, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f'Покупатель {self.id}'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Cart(models.Model):
    """ Корзина товаров """
    owner = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    shop_items = models.ManyToManyField(ProductItem, blank=True)

    def __str__(self):
        return f'Корзина {self.id}'

    class Meta:
        verbose_name = 'Корзина товаров'
        verbose_name_plural = 'Корзины товаров'


class Favorites(models.Model):
    """ Избранные товары """
    owner = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    shop_items = models.ManyToManyField(ProductItem, blank=True)

    def __str__(self):
        return f'Избранные {self.id}'

    class Meta:
        verbose_name = 'Избранный товар'
        verbose_name_plural = 'Избранные товары'
