from rest_framework import serializers

from Consumer.models import Favorites, Cart
from Shop.serializers import ShopItemSerializer


class CartSerializer(serializers.ModelSerializer):
    """ Serializer корзины продуктов """
    shop_items = ShopItemSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):
    """ Serializer корзины продуктов """
    shop_items = ShopItemSerializer(read_only=True, many=True)

    class Meta:
        model = Favorites
        fields = '__all__'
