from django.shortcuts import render
from carousel.models import CmsSlider
from predlogenie.models import Predlogenie
from price.models import Price
from experts.models import Experts
from crm.models import Site
from crm.forms import SiteForm


def index(request):
    slider_list = CmsSlider.objects.all()
    predlogen = Predlogenie.objects.all()
    price = Price.objects.all()
    expert = Experts.objects.all()
    form = SiteForm()
    context = {
        'title': 'Beauty Salon',
        'slider_list': slider_list,
        'predlogen': predlogen,
        'prices': price,
        'experts': expert,
        'form': form
    }
    return render(request, 'shop/index.html', context)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        element = Site(site_name=name, site_email=email, site_phone=phone, site_message=message)
        element.save()
        return render(request, 'shop/thanks.html')
    else:
        return render(request, 'shop/thanks.html')
