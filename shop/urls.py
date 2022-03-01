
from django.urls import path, re_path

from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delivery', views.delivery, name='delivery'),
    path('contacts', views.contacts, name='contacts'),
    re_path(r'^section/(?P<id>\d+)$', views.section, name='section'),
]