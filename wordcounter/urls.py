
from django.urls import path
from . import durga
urlpatterns = [
    path('', durga.home),
    path('count/', durga.count, name='count'),
]


