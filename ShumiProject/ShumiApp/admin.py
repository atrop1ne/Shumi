from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Complaint)
admin.site.register(Card)
admin.site.register(CardImage)
admin.site.register(CardArchive)
admin.site.register(CardStatus)
admin.site.register(Notification)
admin.site.register(NotificationType)
