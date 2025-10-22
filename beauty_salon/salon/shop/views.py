from django.shortcuts import render
from carousel.models import CmsSlider
from predlogenie.models import Predlogenie


def index(request):
    slider_list = CmsSlider.objects.all()
    predlogen = Predlogenie.objects.all()
    context = {
        'title': 'Beauty Salon',
        'slider_list': slider_list,
        'predlogen': predlogen,
    }
    return render(request, 'shop/index.html', context)
