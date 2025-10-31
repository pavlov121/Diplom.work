from django.db import models


class Experts(models.Model):
    exp_img = models.ImageField(upload_to='experts_img/', verbose_name='Изображение')
    exp_title = models.CharField(max_length=200, verbose_name='Заголовок')
    exp_text = models.CharField(max_length=200, verbose_name='Текст')

    def __str__(self):
        return self.exp_title

    class Meta:
        verbose_name = 'Мастер'  # в единственном числе
        verbose_name_plural = 'Мастера'  # Во множественном числе


