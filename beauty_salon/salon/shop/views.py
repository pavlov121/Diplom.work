from django.shortcuts import render
from carousel.models import CmsSlider
from predlogenie.models import Predlogenie
from price.models import Price


def index(request):
    slider_list = CmsSlider.objects.all()
    predlogen = Predlogenie.objects.all()
    price = Price.objects.all()
    context = {
        'title': 'Beauty Salon',
        'slider_list': slider_list,
        'predlogen': predlogen,
        'prices': price
    }
    return render(request, 'shop/index.html', context)
