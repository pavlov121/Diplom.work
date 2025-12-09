from django.shortcuts import render
from .models import Work, WorkCategory, Slider2


def we_done(request, category_id=None):  # Для отображения по категориям
    work = Work.objects.all()
    cat = WorkCategory.objects.all()
    context = {
        'title': 'Работы',
        'works': work,
        'cats': cat
    }
    if category_id:
        context.update({
            'works': Work.objects.filter(category_id=category_id)  # Фильтрация по ID
        })  # Обновляем словарь
    else:
        context.update({
            'works': Work.objects.all()
        })

    return render(request, 'we_done/we-do.html', context)


def usluga(request, pk):
    product_obj = Work.objects.get(id=pk)
    context = {
        'title': product_obj.category,
        'usluga': product_obj,
        'cats': WorkCategory.objects.all(),
        'slider_list': Slider2.objects.all(),
    }
    return render(request, 'we_done/usluga.html', context)

