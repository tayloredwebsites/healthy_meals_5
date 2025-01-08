from django.contrib.auth.models import AbstractUser, UserManager
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from safedelete.managers import SafeDeleteManager


# found example at: https://codeberg.org/mvlaev/Cars/src/branch/main/cars/users_app/models.py
class CustomUserManager(SafeDeleteManager, UserManager):
    pass

class CustomUser(SafeDeleteModel, AbstractUser):
    _safedelete_policy = SOFT_DELETE_CASCADE # should there be no cascase (SOFT_DELETE)?

    objects = CustomUserManager()

    pass

    def __str__(self):
        # fields = [field.name for field in self._meta.fields if field.name != 'password']
        # return ', '.join(f"{field}: {getattr(self, field)}" for field in fields)
        return f'{self.email} - {self.last_name}, {self.first_name}'
