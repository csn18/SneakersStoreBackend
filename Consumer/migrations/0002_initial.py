# Generated by Django 4.1.1 on 2023-07-01 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Seller', '0001_initial'),
        ('Consumer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorites',
            name='shop_items',
            field=models.ManyToManyField(blank=True, to='Seller.productitem'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Consumer.address'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='geolocate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Consumer.geolocate'),
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Consumer.consumer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='shop_items',
            field=models.ManyToManyField(blank=True, to='Seller.productitem'),
        ),
    ]
