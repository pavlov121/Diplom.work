from django.db import models


class StatusCrm(models.Model):
    status_name = models.CharField(max_length=100, verbose_name='Название статуса')  # Дополнительное поле для админа

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'


class Site(models.Model):
    site_dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    site_name = models.CharField(max_length=200, verbose_name='Имя')
    site_email = models.EmailField(max_length=200, verbose_name='Email')
    site_phone = models.CharField(max_length=200, verbose_name='Телефон')
    site_message = models.TextField(max_length=250, verbose_name='Сообщение')
    site_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, blank=True,
                                    null=True, verbose_name='Статус')  # Связь один ко многим, запрещено удаление

    def __str__(self):
        return self.site_name  # Имя

    class Meta:
        verbose_name = 'сообщение/заказ'
        verbose_name_plural = 'сообщения/заказы'
