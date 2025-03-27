from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser

'''username field is the users email

Prevent duplication of email addresses in the CustomUser model at the database level.
see: https://docs.allauth.org/en/latest/
see: https://docs.allauth.org/en/latest/account/configuration.html
# Using a pre_save signal decorator to:
# - force username field to be set to the records email field value for all CustomUser records
'''

@receiver(pre_save, sender=CustomUser)
def email_is_also_username(sender, instance, **kwargs):
    if instance.username != instance.email:
        print(f"{instance.__class__.__name__} changed username from {instance.username} to {instance.email}")
        instance.username = instance.email
