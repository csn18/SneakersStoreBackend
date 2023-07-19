from django_filters import rest_framework as rest_filters, NumberFilter

from Seller.models import ProductItem


class NumberInFilter(rest_filters.BaseInFilter, rest_filters.NumberFilter):
    """ Дополнительный класс фильтрации """
    pass


class ShopItemFilter(rest_filters.FilterSet):
    """ Фильтрация кроссовок """
    brand = NumberInFilter(field_name='brand', lookup_expr='in')
    sizes = NumberInFilter(field_name='sizes', lookup_expr='in')
    price = rest_filters.RangeFilter()

    class Meta:
        model = ProductItem
        fields = ['brand', 'sizes', 'price']
