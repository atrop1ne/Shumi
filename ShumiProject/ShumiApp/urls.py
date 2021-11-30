from django.urls import path
from . import views

urlpatterns = [
    path('main', views.main, name = 'main'),
    path('card_create', views.card_create, name = 'card_create'),
]
