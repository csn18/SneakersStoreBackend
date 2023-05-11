from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.response import Response

from Shop.serializers import (
    ShopItemSerializer, CartSerializer, FavoritesSerializer
)
from Shop.models import ShopItem, Cart, Favorites


class ShopItemView(ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer


class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """ Возвращает корзину пользователя """
        user = self.request.user
        cart = Cart.objects.filter(owner=user.id).first()
        serializer = CartSerializer(cart, context={"request": request})
        return Response(serializer.data)

    def post(self, request, pk=None):
        """ Добавляет товар в корзину """
        user = self.request.user
        shop_item_id = request.data.get('itemId')
        shop_item = ShopItem.objects.filter(id=shop_item_id).first()
        cart = Cart.objects.filter(owner=user.id).first()
        cart.shop_items.add(shop_item)
        return Response(status=status.HTTP_200_OK)


class FirstLoadDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """ Возвращает корзину пользователя """
        user = self.request.user
        total_cost = 0
        cart = Cart.objects.filter(owner=user.id).first()
        favorites = Favorites.objects.filter(owner=user.id).first()
        for item in cart.shop_items.all():
            total_cost += item.price
        return JsonResponse({
            'totalCostCart': round(total_cost, 2),
            'countFavoriteItems': favorites.shop_items.all().count(),
        })


class CartDetailView(APIView):
    def get_object(self, user_id):
        try:
            return Cart.objects.get(owner=user_id)
        except Cart.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        """ Удаляет товар из корзины """
        user = self.request.user
        cart = self.get_object(user.id)
        shop_item = cart.shop_items.filter(id=pk).first()
        cart.shop_items.remove(shop_item)
        return Response(status=status.HTTP_200_OK)


class FavoriteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user_id):
        return Favorites.objects.filter(owner=user_id).first()

    def get(self, request, productId=None):
        """ Возвращает корзину пользователя """
        user = self.request.user
        favorites = self.get_object(user.id)
        serializer = FavoritesSerializer(
            favorites, context={"request": request})
        return Response(serializer.data)

    def post(self, request, productId=None):
        """ Добавляет товар в корзину """
        user = self.request.user
        item_id = request.data.get('itemId')
        shop_item = ShopItem.objects.filter(id=item_id).first()
        favorites = self.get_object(user.id)
        if favorites:
            favorites.shop_items.add(shop_item)
            return Response(status=status.HTTP_200_OK)
        else:
            favorites = Favorites.objects.create(owner_id=user.id)
            favorites.shop_items.add(shop_item)

            return Response(status=status.HTTP_200_OK)


class FavoriteDetailView(APIView):
    def get_object(self, user_id):
        return Favorites.objects.filter(owner=user_id).first()

    def delete(self, request, pk):
        """ Удаляет товар из корзины """
        user = self.request.user
        favorite = self.get_object(user.id)
        if pk:
            shop_item = favorite.shop_items.filter(id=pk).first()
            favorite.shop_items.remove(shop_item)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
