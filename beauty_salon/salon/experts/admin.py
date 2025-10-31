from django.contrib import admin
from .models import Experts
from django.utils.safestring import mark_safe  # Метод, который даёт выводить html-разметку


class ExpertAdmin(admin.ModelAdmin):
    list_display = ('exp_title', 'exp_text', 'get_img')  # какие элементы будут отображаться
    fields = ('exp_title', 'exp_text', 'exp_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f"<img src='{obj.exp_img.url}' width='80'>")

    get_img.short_description = "Миниатюра"


admin.site.register(Experts, ExpertAdmin)
