from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('main', views.main, name = 'main'),
    path('card_create', views.card_create, name = 'card_create'),
    #path('profile', views.profile, name = 'profile'),
    re_path(r'^profile/(?P<id>\w+)$', views.profile, name = 'profile_user'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)