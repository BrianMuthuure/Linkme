from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, User


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create a user profile when a user is created.
    Also creates a profile if the user is updated and doesn't have one.
    """
    if created:
        # Create profile when user is first created
        Profile.objects.create(user=instance)
    else:
        # Ensure profile exists on user update
        if not hasattr(instance, "profile"):
            Profile.objects.get_or_create(user=instance)
