# Generated by Django 4.0.4 on 2022-04-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=20, verbose_name='Цена')),
                ('pc_description', models.CharField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='PriceTabable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_title', models.CharField(max_length=200, verbose_name='Услуга')),
                ('old_price', models.CharField(max_length=200, verbose_name='Старая цена')),
                ('new_price', models.CharField(max_length=200, verbose_name='Новая цена')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
