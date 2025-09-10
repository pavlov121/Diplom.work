from django.shortcuts import render


def main(request):
    return render(request, "main/main.html")


def contact_user(request):
    return render(request, "main/contact.html")
