from django.contrib import admin
from .models import Predlogenie
from django.utils.safestring import mark_safe  # Метод, который даёт выводить html-разметку


class PredAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'get_img')  # какие элементы будут отображаться
    fields = ('cms_title', 'cms_text', 'cms_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f"<img src='{obj.about_img.url}' width='80'>")

    get_img.short_description = "Миниатюра"


admin.site.register(Predlogenie, PredAdmin)

# border: #404040 solid 1px; - Круги для предложения из style.css класса we_box (510 стр)
