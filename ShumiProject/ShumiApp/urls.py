from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('main', views.main, name = 'main'),
    path('card_create', views.card_create, name = 'card_create'),
    path('card_to_archive/<int:card_id>/<str:archive_param>', views.card_to_archive, name = 'card_to_archive')
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)