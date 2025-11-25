from django.contrib import admin
from .models import Work, WorkCategory
from django.utils.safestring import mark_safe  # Метод, который даёт выводить html-разметку


class WorkAdmin(admin.ModelAdmin):
    list_display = ('work_title', 'work_text', 'category', 'work_img')  # какие элементы будут отображаться
    fields = ('work_title', 'work_text', 'category', 'work_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f"<img src='{obj.work_img.url}' width='80'>")

    get_img.short_description = "Миниатюра"


admin.site.register(Work, WorkAdmin)
admin.site.register(WorkCategory)
