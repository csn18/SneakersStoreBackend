from channels.layers import get_channel_layer
from django.db import transaction
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from django.dispatch import receiver

from Consumer.models import Cart
from Consumer.serializers import CartSerializer
from Seller.models import ProductItem
from Shop.serializers import ShopItemSerializer


@receiver(post_save, sender=ProductItem)
def update_product(sender, **kwargs):
    channel_layer = get_channel_layer()
    instance = kwargs['instance']

    if not kwargs['created']:
        async_to_sync(channel_layer.group_send)(
            'room',
            {
                'type': 'update_price_product',
                'typeAction': 'updatePriceProduct',
                'product': ShopItemSerializer(instance).data,
            }
        )


@receiver(post_save, sender=Cart)
def update_cart(sender, **kwargs):
    channel_layer = get_channel_layer()
    instance = kwargs['instance']

    if not kwargs['created']:
        transaction.on_commit(
            lambda: async_to_sync(channel_layer.group_send)(
                'room',
                {
                    'type': 'update_cart',
                    'typeAction': 'updateCart',
                    'cart': CartSerializer(instance).data
                }
            )
        )
