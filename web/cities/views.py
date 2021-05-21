from django.http import HttpResponse
from django.shortcuts import render

from web.cities.models import Person


def index(request):
    context = {
        'name': 'ivo_bass',
        'people': Person.objects.all(),
    }
    return render(request, 'index.html', context)



def list_phones(request):
    return HttpResponse('Phones list')
