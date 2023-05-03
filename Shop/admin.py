from django.contrib import admin
from Shop.models import Sizes, Brand, ShopItem, ItemImage, Cart, Favorites

admin.site.register(Sizes)
admin.site.register(Brand)
admin.site.register(ItemImage)
admin.site.register(Cart)
admin.site.register(Favorites)


class ItemImageInline(admin.TabularInline):
    model = ItemImage


@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]
