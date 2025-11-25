from django.urls import path
from . import views

urlpatterns = [
    path('', views.we_done, name='we_done'),
]