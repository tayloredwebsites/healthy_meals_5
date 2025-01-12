from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser

# Ensure CustomUser email field is not allowed to be duplicated at database level.
# - https://docs.allauth.org/en/latest/
# - https://docs.allauth.org/en/latest/account/configuration.html
# Using a pre_save signal decorator to:
# - force username field to be set to the records email field value for all CustomUser records
@receiver(pre_save, sender=CustomUser)
def email_is_also_username(sender, instance, **kwargs):
    if instance.username != instance.email:
        print(f"{instance.__class__.__name__} changed username from {instance.username} to {instance.email}")
        instance.username = instance.email
