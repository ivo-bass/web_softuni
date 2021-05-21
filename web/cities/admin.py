from django.contrib import admin

from web.cities.models import Person, Phone

admin.site.register(Person)
admin.site.register(Phone)