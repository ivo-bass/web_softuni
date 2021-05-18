from django.contrib import admin
from django.urls import path

from web.cities.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
