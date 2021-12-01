from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name="User photo", null=True, blank=True, upload_to="images/%Y/%m/%d")
    status = models.CharField(verbose_name="User status", null=True, blank=True, max_length=150)
    about = models.TextField(verbose_name="About user", null=True, blank=True)
    contact = models.ManyToManyField("self", verbose_name="Contact", blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
            CardArchive.create_card_archives(Profile.objects.get(user=instance))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class CardArchive(models.Model):
    profile = models.ForeignKey("Profile", verbose_name="Profile", on_delete=models.CASCADE)
    status = models.BooleanField("Card archive status") ##0-Red, 1-Green

    def create_card_archives(current_profile, **kwargs):
        CardArchive.objects.create(profile = current_profile, status=False)
        CardArchive.objects.create(profile = current_profile, status=True)

    def __str__(self):
        return f"{self.profile} " + f"{self.status} " + "CardArchive" 

    class Meta:
        verbose_name = "Card archive"
        verbose_name_plural = "Card archives"

class Category(models.Model):
    name = models.CharField("Category name", max_length=30)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField("Tag name", max_length=30)
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

class Complaint(models.Model):
    profile = models.ForeignKey("Profile", verbose_name="Complaint author", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Complaint date", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Complaint"
        verbose_name_plural = "Complaints"

class CardStatus(models.Model):
    name = models.CharField("Name", max_length=15)

    class Meta:
        verbose_name = "CardStatus"
        verbose_name_plural = "CardStatuses"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SCardStatus_detail", kwargs={"pk": self.pk})


class Card(models.Model):
    owner = models.ForeignKey("Profile", verbose_name="Profile", on_delete=models.CASCADE, related_name="card_owner")
    title = models.CharField(verbose_name="Title", max_length=100, null=True, blank=True)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    participants = models.ManyToManyField("Profile", verbose_name="Participants", blank=True)
    category = models.ForeignKey("Category", verbose_name="Category", on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField("Tag", verbose_name="Tag", blank=True)
    complaint = models.ForeignKey("Complaint", verbose_name="Complaint", null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField("CardStatus", max_length=10, null=True, blank=True)
    max_people_count = models.IntegerField("Card max count of people", default=1)
    archive = models.ManyToManyField("CardArchive", verbose_name="Card archive", blank=True)
    current_people_count = models.IntegerField("Card current count of people", default=0)

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    @property
    def images(self):
        return CardImage.objects.filter(card = self)

class CardImage(models.Model):
    card = models.ForeignKey("Card", verbose_name="Card", on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name="Is main")
    image = models.ImageField(
        verbose_name="Image",
        upload_to="images/%Y/%m/%d"
    )

    class Meta:
        verbose_name = "Card image"
        verbose_name_plural = "Card images"

class NotificationType(models.Model):
    name = models.CharField("NotificationName", max_length=50)

    class Meta:
        verbose_name = "NotificationType"
        verbose_name_plural = "NotificationTypes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("NotificationType_detail", kwargs={"pk": self.pk})


class Notification(models.Model):
    from_profile = models.ForeignKey("Profile", verbose_name="Profile", on_delete=models.CASCADE, related_name="notification_to")
    to_profile = models.ForeignKey("Profile", verbose_name="Profile", on_delete=models.CASCADE, related_name="notification_from")
    notification_type = models.OneToOneField("NotificationType", verbose_name="Notification type", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def get_absolute_url(self):
        return reverse("Notification_detail", kwargs={"pk": self.pk})
