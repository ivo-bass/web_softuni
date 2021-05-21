from django.shortcuts import render

from web.cities.models import Person, Phone


def index(request):
    context = {
        'name': 'ivo_bass',
        'people': Person.objects.all(),
    }
    return render(request, 'index.html', context)


def list_phones(request):
    context = {
        'title': 'Phones List',
        'phones': Phone.objects.all(),
    }
    return render(request, 'phones.html', context)
