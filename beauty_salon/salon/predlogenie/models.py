from django.db import models


class Predlogenie(models.Model):
    cms_img = models.ImageField(upload_to='predlog_img/', verbose_name='Изображение')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Текст')

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'Предложение'  # в единственном числе
        verbose_name_plural = 'Предложения'  # Во множественном числе

