from django.contrib.auth.models import AbstractUser, UserManager
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from safedelete.managers import SafeDeleteManager

# Mix in SafeDeleteManager into CustomUserManager for Soft Deletes using safedelete
# - https://django-safedelete.readthedocs.io/en/latest/managers.html
# safe delete of custom users example found at;
# - https://codeberg.org/mvlaev/Cars/src/branch/main/cars/users_app/models.py
class CustomUserManager(SafeDeleteManager, UserManager):

    def all_deleted(self):
        return self.all_with_deleted().filter(deleted__isnull=False)

# Mix in SafeDeleteModel into CustomUser Model for Soft Deletes using safedelete
# - https://django-safedelete.readthedocs.io/en/latest/managers.html

class CustomUser(SafeDeleteModel, AbstractUser):
    _safedelete_policy = SOFT_DELETE_CASCADE # To Do: research/test if there should be no cascading of deletes (SOFT_DELETE)?

    objects = CustomUserManager()

    pass

    def __str__(self):
        # fields = [field.name for field in self._meta.fields if field.name != 'password']
        # return ', '.join(f"{field}: {getattr(self, field)}" for field in fields)
        return f'{self.email} - {self.last_name}, {self.first_name}'
