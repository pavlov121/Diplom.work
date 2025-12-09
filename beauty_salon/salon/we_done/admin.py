from django.contrib import admin
from .models import Work, WorkCategory, Slider2
from django.utils.safestring import mark_safe  # Метод, который даёт выводить html-разметку


class WorkAdmin(admin.ModelAdmin):
    list_display = ('work_title', 'work_text', 'category', 'description', 'get_img')  # какие элементы будут отображаться
    fields = ('work_title', 'work_text', 'category', 'work_img', 'description', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f"<img src='{obj.work_img.url}' width='80'>")

    get_img.short_description = "Миниатюра"


class Slider2Admin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_cat', 'cms_css', 'get_img')  # какие элементы будут отображаться
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_cat', 'cms_css', 'cms_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f"<img src='{obj.cms_img.url}' width='80'>")

    get_img.short_description = "Миниатюра"


admin.site.register(Work, WorkAdmin)
admin.site.register(WorkCategory)
admin.site.register(Slider2, Slider2Admin)
