from django.shortcuts import render
from .models import Work, WorkCategory


def we_done(request):
    work = Work.objects.all()
    cat = WorkCategory.objects.all()
    context = {
        'title': 'Работы',
        'works': work,
        'cats': cat
    }
    return render(request, 'we_done/we-do.html', context)
