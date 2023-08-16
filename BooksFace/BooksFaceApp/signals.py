from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from BooksFace.BooksFaceApp.models import Profile


@receiver(signal=post_save, sender=User)
def after_created_user(sender, instance, created, **kwargs):

    if created:
        profile = Profile.objects.create(user=instance)
        if instance.first_name and not instance.last_name:
            profile.first_name = instance.first_name
            profile.save()
        elif instance.last_name and not instance.first_name:
            profile.last_name = instance.last_name
            profile.save()
        elif instance.first_name and instance.last_name:
            profile.first_name = instance.first_name
            profile.last_name = instance.last_name
            profile.save()


@receiver(signal=post_save, sender=Profile)
def after_updated_profile(sender, instance, created, **kwargs):
    if not created:
        user = instance.user
        if instance.first_name and not instance.last_name:
            user.first_name = instance.first_name
            user.save()
        elif instance.last_name and not instance.first_name:
            user.last_name = instance.last_name
            user.save()
        elif instance.first_name and instance.last_name:
            user.first_name = instance.first_name
            user.last_name = instance.last_name
            user.save()


@receiver(signal=post_delete, sender=Profile)
def after_delete_profile(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()



