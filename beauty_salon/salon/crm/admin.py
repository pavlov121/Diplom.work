from django.contrib import admin
from .models import StatusCrm, Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_status', 'site_name', 'site_phone', 'site_dt')
    list_editable_links = ('id', 'site_name')
    search_fields = ('id', 'site_name', 'site_phone', 'site_dt')
    list_per_page = 4


admin.site.register(StatusCrm)
admin.site.register(Site, SiteAdmin)
