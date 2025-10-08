from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("company/<str:pk>/", views.company, name="company"),  # подключение компании
    path("contact/", views.contact_user, name="contact"),  # подключение contact
    path("about/", views.about, name="about")  # подключение about
]

