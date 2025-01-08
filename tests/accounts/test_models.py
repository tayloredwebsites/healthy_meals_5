from django.test import TestCase

from .factories import CustomUserFactory

from accounts.models import CustomUser

class UserModelsTestCase(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_user_soft_delete(self):
        # get starting user record count
        count = CustomUser.objects.count()
        # confirm no users
        assert count == 0
        # create 4 test users
        test_users = CustomUserFactory.create_batch(4)
        # confirm we now have 4 more
        assert count + 4 == CustomUser.objects.count()
        print(f'As Created: {test_users[0].email}: {test_users[0].username}, {test_users[0].deleted}')
        # soft delete the first user
        test_users[0].delete()
        print(f'Soft Deleted: {test_users[0].email}: {test_users[0].username}, {test_users[0].deleted}')
        # confirm we have one less
        assert CustomUser.objects.count() == 3
        ## Note there is no database check for duplicate email prevention.
        # To Do: all user creates and updates of email address must be coded to prevent duplicate email
        # To Do: consider having an admin tool to validate no duplicate email addresses
        # create a new user with matching email from first record
        new_user = CustomUserFactory(
            email=test_users[0].email,
            first_name=test_users[0].first_name,
            last_name=test_users[0].last_name,
        )
        print(f'Duplicate Email User Created: {new_user.email}: {new_user.username}, {new_user.deleted}')
        assert CustomUser.objects.count() == 4
        # soft delete duplicate email user
        new_user.delete()
        assert CustomUser.objects.count() == 3
        # restore the soft deleted user
        test_users[0].undelete()
        assert CustomUser.objects.count() == 4
        print(f'Restored: {test_users[0].email}: {test_users[0].username}, {test_users[0].deleted}')
