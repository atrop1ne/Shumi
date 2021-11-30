from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

def main(request):
    user = User.objects.get(pk = request.user.pk)
    cards = Card.objects.filter(owner = user.profile)

    context = {
        'title' : 'Главная',
        'cards' : cards
    }

    return render(request, "ShumiApp/main.html", context)

def card_create(request):
    user = User.objects.get(pk = request.user.pk)

    if request.method == "POST":
        card = Card()
        card.owner = user.profile
        card.title = request.POST.get("card_title")
        card.description = request.POST.get("card_description")
        card.save()
        # return redirect('main')
    else:
        return render(request, "ShumiApp/card_create_page.html", {'title': 'Создать карточку'})
