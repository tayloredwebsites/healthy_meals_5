from factory import Faker, django
from accounts import models

class CustomUserFactory(django.DjangoModelFactory):
    class Meta:
        model = models.CustomUser
    username = Faker('user_name')
    email = Faker('email')
    password=Faker('password')
    last_name=Faker('first_name')
    first_name=Faker('last_name')
    # deleted=None
