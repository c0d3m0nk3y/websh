from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('hijack', Hijack.as_view(), name='hijack'),
]
