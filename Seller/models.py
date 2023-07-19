from django.db import models

from Auth.models import User


class Seller(User):
    """ Продавец """
    fio = models.CharField('ФИО', max_length=255)
    phone = models.CharField('Телефон', max_length=11, blank=True)

    def __str__(self):
        return f'Продавец {self.id}'

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class ProductSizes(models.Model):
    """ Размеры товаров """
    size = models.PositiveIntegerField('Размер')

    def __str__(self):
        return f'Размер {self.id}'

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class ProductBrand(models.Model):
    """ Бренды товаров """
    brand_name = models.CharField('Название бренда', max_length=255)

    def __str__(self):
        return f'Бренд {self.id}'

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class ProductItem(models.Model):
    """ Товар """
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    title = models.CharField('Название товара', max_length=255)
    desc = models.TextField('Описание', max_length=4096, blank=True)
    price = models.DecimalField('Стоимость', decimal_places=2, max_digits=12)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(ProductSizes)
    count = models.PositiveIntegerField('Количество (шт)')

    def __str__(self):
        return f'Товар {self.id}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    """ Фотографии товара """
    item = models.ForeignKey(
        ProductItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Фотография', upload_to='image')

    def __str__(self):
        return f'Фотография {self.id}'

    class Meta:
        verbose_name = 'Фотография товара'
        verbose_name_plural = 'Фотографии товаров'
