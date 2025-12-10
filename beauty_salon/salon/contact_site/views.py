from django.shortcuts import render


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'contact_site/contact.html', context)
