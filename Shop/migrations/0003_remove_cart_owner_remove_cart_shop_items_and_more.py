# Generated by Django 4.1.1 on 2023-07-01 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_alter_cart_shop_items_alter_favorites_shop_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='shop_items',
        ),
        migrations.RemoveField(
            model_name='favorites',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='favorites',
            name='shop_items',
        ),
        migrations.RemoveField(
            model_name='itemimage',
            name='item',
        ),
        migrations.RemoveField(
            model_name='shopitem',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='shopitem',
            name='sizes',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
        migrations.DeleteModel(
            name='ItemImage',
        ),
        migrations.DeleteModel(
            name='ShopItem',
        ),
        migrations.DeleteModel(
            name='Sizes',
        ),
    ]
