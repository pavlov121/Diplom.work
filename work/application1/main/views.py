from django.shortcuts import render
from .models import Main2


def main(request):
    mn = Main2.objects.all()
    context = {
        'main': mn
    }
    return render(request, "main/main.html", context)


def contact_user(request):
    return render(request, "main/contact.html")
