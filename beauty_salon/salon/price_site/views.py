from django.shortcuts import render
from .models import Price


def price_cena(request):
    price = Price.objects.all()
    context = {
        'title': 'Цены',
        'prices': price
    }
    return render(request, 'price_site/pricing.html', context)

