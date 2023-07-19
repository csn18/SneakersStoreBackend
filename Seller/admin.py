from django.contrib import admin

from Seller.models import (
    Seller, ProductItem, ProductBrand, ProductSizes, ProductImage
)

admin.site.register(ProductBrand)
admin.site.register(ProductSizes)


class ProductImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


@admin.register(Seller)
class AdminSeller(admin.ModelAdmin):
    fieldsets = (
        (
            'Авторизация', {
                'fields': [
                    'email', 'password'
                ]
            }
        ),
        (
            'Личные данные', {
                'fields': [
                    'phone', 'fio'
                ]
            }
        ),
    )

    add_fieldsets = (
        (
            None, {
                'classes': ['wide'],
                'fields': [
                    'email', 'password1', 'password2'
                ]
            }
        ),
    )
