from rest_framework import serializers
from Shop.models import ShopItem, ItemImage, Cart, Favorites


class ShopItemImagesSerializers(serializers.ModelSerializer):
    """ Serializer фотографий продукта """
    image = serializers.SerializerMethodField()

    class Meta:
        model = ItemImage
        fields = ['id', 'image']

    def get_image(self, item):
        request = self.context.get('request')
        if request:
            image = item.image.url
            return request.build_absolute_uri(image)
        else:
            # Временное решение
            return f'http://localhost:8000{item.image.url}'


class ShopItemSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer продукта """
    brand = serializers.SlugRelatedField(
        slug_field='brand_name', read_only=True)
    sizes = serializers.SlugRelatedField(
        slug_field='size', read_only=True, many=True)
    images = ShopItemImagesSerializers(many=True)

    class Meta:
        model = ShopItem
        fields = [
            'id', 'title', 'description', 'price', 'brand', 'sizes', 'images'
        ]


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
