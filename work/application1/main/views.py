from django.shortcuts import render
from .models import Company, Room
from cms.models import CmsSlider


def main(request):
    slider_list = CmsSlider.objects.all()
    rm = Room.objects.all()  # получаем все данные
    context = {
        'rooms': rm,
        'slider_list': slider_list
    }

    return render(request, "main/main.html", context)


def company(request, pk):
    cm = Company.objects.get(id=pk)
    context = {
        'company': cm,
    }
    return render(request, "main/company.html", context)


def about(request):
    return render(request, "main/property-details.html")


def contact_user(request):
    return render(request, "main/contact.html")
