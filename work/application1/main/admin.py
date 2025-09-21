from django.contrib import admin
from .models import Main2, Main, City, Room, Company

# admin.site.register(Main2)  # отображение в админ панели
# admin.site.register(Main)
# admin.site.register(City)
admin.site.register(Room)
admin.site.register(Company)

