from django.urls import path
from . import views

urlpatterns = [
    path('', views.we_done, name='we_done'),
    path('products/<int:category_id>/', views.we_done, name='cat'),  # Вывод меню категорий
    path('product/<int:pk>/', views.usluga, name='usluga'),  # Вывод отдельной страницы
]