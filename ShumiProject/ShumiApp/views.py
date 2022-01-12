from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

def main(request):
    current_archive_yes = CardArchive.objects.get(profile=request.user.profile, status=1)
    current_archive_no = CardArchive.objects.get(profile=request.user.profile, status=0)
    cards = Card.objects.exclude(
        owner = request.user.profile).exclude(
            archive = current_archive_yes).exclude(
                archive = current_archive_no).reverse()

    context = {
        'title' : 'Главная',
        'cards' : cards
    }

    return render(request, "ShumiApp/main.html", context)

def card_delete(request, card_id):
    card = Card.objects.get(id = card_id)
    if card.owner == request.user.profile:
        card.delete()

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
        return redirect('profile/my')
    else:
        return render(request, "ShumiApp/card_create_page.html", {'title': 'Создать карточку'})

def profile(request, id):
    my = False
    if id == "my" :
        user = User.objects.get(pk = request.user.pk)
        my = True

    else: 
        user = User.objects.get(pk = int(id))

    if user.pk == request.user.pk:
        my = True

    cards = Card.objects.filter(owner = user.profile)
    contacts = Profile.objects.filter(contact = user.profile)

    context = {
        'title' : 'Профиль',
        'user' : user,
        'my' : my,
        'cards' : cards,
        'contacts' : contacts,
    }

    return render(request, "ShumiApp/profile.html", context)

def contact_manipulation(request, id, contact_operation_param):
    try:
        profile_on_change_status = Profile.objects.get(id = id)
        current_profile = Profile.objects.get(user = request.user)
    except:
        pass

    if contact_operation_param == 'add':
        current_profile.contact.add(profile_on_change_status)
    else:
        current_profile.contact.remove(profile_on_change_status)

    current_profile.save()


def card_to_archive(request, card_id, archive_param):
    user = User.objects.get(pk = request.user.pk)
    card = Card.objects.get(id = card_id)

    current_yes_archive = CardArchive.objects.get(profile = user.profile, status = 1)
    current_no_archive = CardArchive.objects.get(profile = user.profile, status = 0)

    if archive_param == "no":
        card.archive.add(current_no_archive)
        try:
            card.archive.remove(current_yes_archive)
        except:
            pass

    else:
        card.archive.add(current_yes_archive)
    card.save()

def archive(request):
    current_archive = CardArchive.objects.get(profile=request.user.profile, status=1)
    cards = Card.objects.filter(archive = current_archive)
    context = {
        'title' : 'Архив',
        'cards' : cards,
    }
    return render(request, "ShumiApp/archive.html", context)

def card_remove_from_archive(request, card_id):
    current_archive = CardArchive.objects.get(profile=request.user.profile, status=1)
    card = Card.objects.get(id = card_id)
    card.archive.remove(current_archive)
    card.save()