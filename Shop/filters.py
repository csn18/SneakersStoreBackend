from django_filters import rest_framework as filters
from .models import ShopItem


class CharFieldInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShopItemFilter(filters.FilterSet):
    brand = CharFieldInFilter(field_name='brand', lookup_expr='in')

    class Meta:
        model = ShopItem
        fields = ['brand']
