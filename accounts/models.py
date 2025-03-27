from django.contrib.auth.models import AbstractUser, UserManager
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from safedelete.managers import SafeDeleteManager
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField


""" Accounts model for storing users customized to allow login by email, etc.
[Source: https://toxigon.com]
Mix in SafeDeleteManager into CustomUserManager for Soft Deletes using safedelete
- https://django-safedelete.readthedocs.io/en/latest/managers.html
safe delete of custom users example found at;
- https://codeberg.org/mvlaev/Cars/src/branch/main/cars/users_app/models.py"
"""

class CustomUserManager(SafeDeleteManager, UserManager):
    """Custom User model Manager class ('objects').

    Manager class for CustomUsers (Accounts).  Access to this class is through the 'objects'
    instance attribute of the CustomUser Class.

    Soft Delete of Users are implemented through SafeDelete.
    See: https://django-safedelete.readthedocs.io/en/latest/managers.html

    Args:
    param1 (class): SafeDelete manager class mixin
    param2 (class): UserManager  for CustomUser Abstract Class

    Attributes:
    param1 (class): SafeDelete manager class mixin
    param2 (class): UserManager  for CustomUser Abstract Class

    """
    def all_deleted(self):
        """Returns all soft deleted customuser records.

        No arguments are passed to this function when calling it

        Returns:
        recordset: The soft deleted custom user records.

        Example:

        .. code-block:: python

            for rec in Account.all_deleted():
                print(rec)

        """
        return self.all_with_deleted().filter(deleted__isnull=False)

# Mix in SafeDeleteModel into CustomUser Model for Soft Deletes using safedelete
# - https://django-safedelete.readthedocs.io/en/latest/managers.html

class CustomUser(SafeDeleteModel, AbstractUser):
    '''CustomUser model - Abstract User customized to allow login by email
    '''

    history = AuditlogHistoryField()

    _safedelete_policy = SOFT_DELETE_CASCADE # To Do: research/test if there should be no cascading of deletes (SOFT_DELETE)?

    objects = CustomUserManager()

    def rec_history_count(self):
        return self.history.all().count()

    def rec_history_field_was(self, user_rec, field_name):
        rec = self.history.all()[user_rec]
        return self.__get_field_changes(rec,field_name)[0]

    def rec_history_field_is_now(self, user_rec, field_name):
        rec = self.history.all()[user_rec]
        return self.__get_field_changes(rec,field_name)[1]

    def rec_history_field_changed(self, user_rec, field_name):
        rec = self.history.all()[user_rec]
        changes = self.__get_field_changes(rec,field_name)
        # print(f'changes: {changes}')
        return changes[0] != changes[1]

    def __get_field_changes(self, hist_rec, field_name):
        try:
            changes = hist_rec.changes_dict[field_name]
            # print(f'changes: {changes}')
            return changes
        except KeyError as e:
            # there was no change, audit log does not log values that do not change, so return array of None strings
            print(f'expected key error auditlog - no changes for field: {e}')
            return ['None', 'None']

    def name_or_email(self):
        if self.first_name != '' and self.last_name != '':
            return "{fname} {lname}".format(fname=self.first_name, lname=self.last_name)
        else:
            print(f'missing full name, using user email: {self.email}')
            return self.email
    pass

    def __str__(self):
        # fields = [field.name for field in self._meta.fields if field.name != 'password']
        # return ', '.join(f"{field}: {getattr(self, field)}" for field in fields)
        return f'{self.email} - {self.last_name}, {self.first_name}'

# place as last line in file to ensure it gets all changes into AuditLog
auditlog.register(CustomUser, exclude_fields=[
    'password', # protect this field for security reasons
    'last_login', # do not update audit log for each login
    ],
)
