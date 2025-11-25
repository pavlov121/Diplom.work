from django.db import models


class Price(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Стоимость")  # Вещественное число!
    price_img = models.ImageField(upload_to='price_img/', blank=True, verbose_name='Изображение')
    price_title = models.CharField(max_length=200, verbose_name='Заголовок')
    price_text = models.CharField(max_length=200, verbose_name='Описание', default="Art Beauty")

    def __str__(self):
        return self.price_title

    class Meta:
        verbose_name = 'Цена'  # в единственном числе
        verbose_name_plural = 'Цены'  # Во множественном числе
