from rest_framework import serializers

from Consumer.models import Cart, Favorites
from Seller.models import ProductImage, ProductItem, ProductBrand, \
    ProductSizes, Seller


class ShopItemImagesSerializers(serializers.ModelSerializer):
    """ Serializer фотографий продукта """

    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class SellerSerializers(serializers.ModelSerializer):
    """ Serializer продавца """

    class Meta:
        model = Seller
        fields = ['id', 'fio', 'phone']


class ShopItemSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer продукта """
    brand = serializers.SlugRelatedField(
        slug_field='brand_name', read_only=True)
    sizes = serializers.SlugRelatedField(
        slug_field='size', read_only=True, many=True)
    images = ShopItemImagesSerializers(many=True)
    seller = SellerSerializers(many=False)

    class Meta:
        model = ProductItem
        fields = [
            'id', 'title', 'desc', 'price', 'brand', 'sizes', 'images',
            'seller'
        ]


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = ['id', 'brand_name']


class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSizes
        fields = ['id', 'size']

