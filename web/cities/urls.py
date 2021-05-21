# cities.urls


from django.urls import path

from web.cities.views import index, list_phones

urlpatterns = [
    path('', index),
    path('phones/', list_phones)
]
