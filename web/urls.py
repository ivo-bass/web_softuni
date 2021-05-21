from django.contrib import admin
from django.urls import path, include

from web.cities.views import index

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),

    path('cities/', include('web.cities.urls')),
    path('poeple/', include('web.people.urls')),
]
