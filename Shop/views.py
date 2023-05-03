from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.response import Response

from Shop.serializers import ShopItemSerializer, CartSerializer
from Shop.models import ShopItem, Cart


class ShopItemView(ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """ Возвращает корзину пользователя """
        user = self.request.user
        cart = Cart.objects.filter(owner=user.id).first()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request, pk=None):
        """ Добавляет товар в корзину """
        user = self.request.user
        shop_item_id = request.data.get('itemId')
        shop_item = ShopItem.objects.filter(id=shop_item_id).first()
        cart = Cart.objects.filter(owner=user.id).first()
        cart.shop_items.add(shop_item)
        return Response(status=status.HTTP_200_OK)


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
