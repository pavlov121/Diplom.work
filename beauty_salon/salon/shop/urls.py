from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thanks', views.thanks_page, name='thanks_page'),
]
