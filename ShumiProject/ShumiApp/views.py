from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

def main(request):
    cards = Card.objects.all()

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
        return redirect('profile_user')
    else:
        return render(request, "ShumiApp/card_create_page.html", {'title': 'Создать карточку'})

def profile(request, id):
    my = False
    if id == "my" :
        user = User.objects.get(pk = request.user.pk)
        my = True

    else: 
        user = User.objects.get(pk = int(id))

    cards = Card.objects.filter(owner = user.profile)

    context = {
        'title' : 'Профиль',
        'user' : user,
        'my' : my,
        'cards' : cards,
    }

    return render(request, "ShumiApp/profile.html", context)

def card_to_archive(request, card_id, archive_param):
    user = User.objects.get(pk = request.user.pk)
    card = Card.objects.get(id = card_id)
    archive_status = 1

    if archive_param == "no":
        archive_status = 0

    current_archive = CardArchive.objects.get(profile = user.profile, status = archive_status)

    card.archive.add(current_archive)
    card.save()

def archive(request):
    current_archive = CardArchive.objects.get(profile=request.user.profile, status=1)
    cards = Card.objects.filter(archive = current_archive)
    context = {
        'title' : 'Архив',
        'cards' : cards,
    }
    return render(request, "ShumiApp/archive.html", context)