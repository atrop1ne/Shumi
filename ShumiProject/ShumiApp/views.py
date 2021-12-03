from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

def welcome(request):
    context = {'title': 'Добро пожаловать'}
    return render(request, 'ShumiApp/welcome.html', context)

def main(request):
    cards = Card.objects.all()

    context = {
        'title' : 'Главная',
        'cards' : cards
    }

    return render(request, "ShumiApp/main.html", context)

def profile(request, id):
    
    if id == "my" :
        user = User.objects.get(pk = request.user.pk)

    else: 
        user = User.objects.get(pk = int(id))
        
    context = {
        'title' : 'Профиль',
    }

    return render(request, "ShumiApp/profile.html", context)


def card_create(request):
    user = User.objects.get(pk = request.user.pk)

    if request.method == "POST":
        card = Card()
        card.owner = user.profile
        card.title = request.POST.get("card_title")
        card.description = request.POST.get("card_description")
        max_people_count = request.POST.get("card_max_people_count")
        if max_people_count:
            card.max_people_count = max_people_count
        card.save()
        images = request.FILES.getlist("card_images")
        if images:
            for image in images:
                card_image = CardImage()
                card_image.card = card
                card_image.is_main = False
                card_image.image = image
                card_image.save()
        card.save()
        # return redirect('main')
    else:
        return render(request, "ShumiApp/card_create_page.html", {'title': 'Создать карточку'})
