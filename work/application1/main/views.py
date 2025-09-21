from django.shortcuts import render
from .models import Main2, Main, City, Company, Room


def main(request):
    # mn = Main2.objects.all()
    # mn2 = Main.objects.all()
    # context = {
    #     'main': mn,
    #     'main2': mn2
    # }
    rm = Room.objects.all()
    cm = Company.objects.all()
    context = {
        'rooms': rm,
        'company': cm
    }

    return render(request, "main/main.html", context)


def contact_user(request):
    return render(request, "main/contact.html")


def company(request):
    return render(request, "main/company.html")
