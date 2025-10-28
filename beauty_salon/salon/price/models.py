from Scripts.bottle import request
from django.db import models


class Price(models.Model):
    price = models.IntegerField(default=0, verbose_name="Стоимость")
    price_img = models.ImageField(upload_to='price_img/', verbose_name='Изображение')
    price_title = models.CharField(max_length=200, verbose_name='Заголовок')
    price_text = models.CharField(max_length=200, verbose_name='Описание', default="Art Beauty")

    def __str__(self):
        return self.price_title

    class Meta:
        verbose_name = 'Цена'  # в единственном числе
        verbose_name_plural = 'Цены'  # Во множественном числе

