from django.contrib.auth.models import User
from .models import ProfileModel
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)
