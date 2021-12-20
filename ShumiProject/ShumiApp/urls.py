from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from allauth.account import views as allauth_views

urlpatterns = [
    path('', allauth_views.login, name="account_login"),
    re_path(r"^logout/$", allauth_views.logout, name="account_logout"),

    path('main', views.main, name = 'main'),
    path('card_create', views.card_create, name = 'card_create'),
    re_path(r'^profile/(?P<id>\w+)$', views.profile, name = 'profile_user'),
    path('card_to_archive/<int:card_id>/<str:archive_param>', views.card_to_archive, name = 'card_to_archive')
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)