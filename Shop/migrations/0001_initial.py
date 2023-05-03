# Generated by Django 4.2 on 2023-04-21 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Название бренда')),
            ],
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveIntegerField(verbose_name='Размер')),
            ],
        ),
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description', models.TextField(max_length=4096, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Стоимость')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.brand', verbose_name='Бренд')),
                ('sizes', models.ManyToManyField(to='Shop.sizes', verbose_name='Размеры')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image', verbose_name='Фотография')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.shopitem', verbose_name='')),
            ],
        ),
    ]
