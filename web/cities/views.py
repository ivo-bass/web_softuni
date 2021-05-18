from django.shortcuts import render

from web.cities.models import Person


def index(request):
    context = {
        'name': 'ivo_bass',
        'people': Person.objects.all(),
    }
    return render(request, 'index.html', context)
