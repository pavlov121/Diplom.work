from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название квартира")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")
    short_description = models.CharField(max_length=100, blank=True, verbose_name="Краткое описание")
    Area = models.CharField(max_length=200, verbose_name='Площадь квартиры')
    Floor = models.IntegerField(default=0, verbose_name='Этаж')
    year = models.IntegerField(default=0, verbose_name='Год постройки')
    Parking = models.CharField(max_length=200, verbose_name='Парковка')
    image = models.ImageField(upload_to="main/%Y/%m/%d/", blank=True,
                              default="run.jpg",
                              verbose_name="Изображение квартиры")  # Изображение (создание папки с датой создания)
    company = models.ForeignKey('Company', on_delete=models.CASCADE,
                                verbose_name="Компания")  # К одной квартире много компаний

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'квартира'
        verbose_name_plural = 'квартиры'


class Company(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название компании')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to="main/%Y/%m/%d/", blank=True,
                              default="run.jpg",
                              verbose_name='Логотип компании')  # Изображение (создание папки с датой создания)
    demo_link = models.CharField(max_length=2000, blank=True, verbose_name='Ссылка')  # Подробная информация

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'


class Eco(models.Model):
    image2 = models.ImageField(upload_to="main/%Y/%m/%d/", blank=True,
                               default="run.jpg")
    category = models.CharField(max_length=200)



