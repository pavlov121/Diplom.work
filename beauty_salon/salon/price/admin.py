from django.contrib import admin
from .models import Price
from django.utils.safestring import mark_safe  # Метод, который даёт выводить html-разметку


class PriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'price_title', 'price_text', 'get_img')  # какие элементы будут отображаться
    fields = ('price', 'price_title', 'price_text', 'price_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f"<img src='{obj.price_img.url}' width='80'>")

    get_img.short_description = "Миниатюра"


admin.site.register(Price, PriceAdmin)