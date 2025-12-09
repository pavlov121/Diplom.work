from django.db import models


class WorkCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Категория работ')
    description = models.TextField(blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'  # в единственном числе
        verbose_name_plural = 'Категории'  # Во множественном числе


class Work(models.Model):
    work_img = models.ImageField(upload_to='work_img/', verbose_name='Изображение')
    work_title = models.CharField(max_length=200, verbose_name='Заголовок')
    work_text = models.TextField(max_length=300, blank=True, verbose_name='Краткое Описание')
    category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE, verbose_name="Категория", default='')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')


    def __str__(self):
        return self.work_title

    class Meta:
        verbose_name = 'Работа'  # в единственном числе
        verbose_name_plural = 'Работы'  # Во множественном числе


class Slider2(models.Model):
    cms_img = models.ImageField(upload_to='slide2_img/', verbose_name='Изображение')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_css = models.CharField(max_length=20, default='-', verbose_name='CSS класс')
    cms_cat = models.ForeignKey(Work, on_delete=models.CASCADE, verbose_name="Название работы", default='')

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'слайд по работе'  # в единственном числе
        verbose_name_plural = 'слайды по работам'  # Во множественном числе
