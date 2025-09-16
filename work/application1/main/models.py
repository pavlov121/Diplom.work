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
