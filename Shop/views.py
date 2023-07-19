from django.db.models import Max, Min
from django.http import Http404, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from Consumer.models import Cart, Favorites
from Seller.models import ProductItem, ProductBrand, ProductSizes
from Shop.filters import ShopItemFilter
from Shop.serializers import (
    ShopItemSerializer, FilterSerializer,
    SizesSerializer
)


class ShopItemPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class ShopItemView(ModelViewSet):
    queryset = ProductItem.objects.all().distinct()
    serializer_class = ShopItemSerializer
    pagination_class = ShopItemPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShopItemFilter


class FirstLoadDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """ Возвращает корзину пользователя """
        user = self.request.user
        cart = Cart.objects.filter(owner=user.id).first()
        favorites = Favorites.objects.filter(owner=user.id).first()
        total_cost = sum([item.price for item in cart.shop_items.all()])

        favorite_items = list(favorites.shop_items.all().values('id', 'title'))
        cart_items = list(cart.shop_items.all().values('id', 'title'))
        total_cost = round(total_cost, 2)

        return JsonResponse({
            'favoriteItemsId': favorite_items,
            'totalCostCart': total_cost,
            'cartItemsId': cart_items,
        })


class FilterList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """ Получение данных для первой загрузки """
        all_brands = ProductBrand.objects.all()
        all_sizes = ProductSizes.objects.all()
        serializer_brands = FilterSerializer(all_brands, many=True).data
        serializer_sizes = SizesSerializer(all_sizes, many=True).data
        max_price = ProductItem.objects.aggregate(
            Max('price')).get('price__max')
        min_price = ProductItem.objects.aggregate(
            Min('price')).get('price__min')

        return JsonResponse({
            'brands': serializer_brands,
            'sizes': serializer_sizes,
            'max_price': int(max_price),
            'min_price': int(min_price),
        })
