from django.urls import path
from .views import index, contato, sobre, localizacao

urlpatterns= [
    path('',index),
    path('index',index),
    path('contato',contato),
    path('sobre',sobre),
    path('localizacao',localizacao),
]