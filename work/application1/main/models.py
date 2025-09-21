from django.db import models


class Main2(models.Model):
    title = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Main(models.Model):
    title = models.CharField(max_length=200)  # Название Соревнования
    description = models.TextField(blank=True)  # Описание
    image = models.ImageField(upload_to="main/%Y/%m/%d/", blank=True,
                              default="run.jpg")  # Изображение (создание папки с датой создания)
    demo_link = models.CharField(max_length=2000, blank=True)  # Подробная информация о марафоне
    city = models.ManyToManyField('City', blank=True)  # Связь многие ко многим: К одному марафону, несколько городов
    uch = models.IntegerField(default=0)  # Количество участников
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class City(models.Model):  # Города в которых проводится данный марафон
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    title = models.CharField(max_length=200)  # Для определения
    address = models.CharField(max_length=200)  # Адрес
    money = models.CharField(max_length=200)  # Стоимость
    Bedrooms = models.IntegerField(default=0)    # Спальная комната
    Bathrooms = models.IntegerField(default=0)   # Ванная комната
    Area = models.CharField(max_length=200)  # Площадь
    Floor = models.IntegerField(default=0)    # Этаж
    Parking = models.CharField(max_length=200)  # Парковка
    image = models.ImageField(upload_to="main/%Y/%m/%d/", blank=True,
                              default="run.jpg")  # Изображение (создание папки с датой создания)
    Company = models.ManyToManyField('Company', blank=True)  # К одной квартире много компаний

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=200)  # Название компании
    description = models.TextField(blank=True)  # Описание
    image = models.ImageField(upload_to="main/%Y/%m/%d/", blank=True,
                              default="run.jpg")  # Изображение (создание папки с датой создания)
    demo_link = models.CharField(max_length=2000, blank=True)  # Подробная информация

    def __str__(self):
        return self.title


