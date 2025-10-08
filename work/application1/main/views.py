from django.shortcuts import render
from .models import Company, Room


def main(request):
    # mn = Main2.objects.all()
    # mn2 = Main.objects.all()
    # context = {
    #     'main': mn,
    #     'main2': mn2
    # }
    rm = Room.objects.all()  # получаем все данные
    context = {
        'rooms': rm,
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
