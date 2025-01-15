from django.test import TestCase

from .factories import CustomUserFactory

from accounts.models import CustomUser

from django.db import IntegrityError, transaction

# using testcase with factoryboy for testing updates to the database
# run as one test to minimize database setup and teardown
class UserModelsTestCase(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    # test to make sure that
    # - soft deletes and undeletes update the database properly,
    # - emails are ensured to be unique,
    # - CustomUser prints out as expected,
    # - all_deleted (custom function) return the deleted custom users
    def test_user_soft_delete(self):
        # get starting user record count
        count = CustomUser.objects.count()
        # confirm no users
        assert count == 0
        # create 4 test users
        test_users = CustomUserFactory.create_batch(4)
        # confirm we now have 4 more
        assert count + 4 == CustomUser.objects.count()
        user0 = test_users[0]
        # ensure print output of CustomUser is correct
        self.assertEqual(user0.__str__(), f'{user0.email} - {user0.last_name}, {user0.first_name}')
        print(f'As Created: {user0.email}: {user0.username}, {user0.deleted}')
        # soft delete the first user
        user0.delete()
        print(f'Soft Deleted: {user0.email}: {user0.username}, {user0.deleted}')
        for rec in CustomUser.objects.all_with_deleted():
            print(f'After soft delete record 0: {rec.email}: {rec.username}, {rec.deleted}')
        # confirm we have one less
        self.assertEqual(CustomUser.objects.all_with_deleted().count(), 4)
        self.assertEqual(CustomUser.objects.all_deleted().count(), 1)

        # make sure the database does not allow duplicate emails for custom_users
        # tests the pre_save signal that copies the email into the username field
        # - this ensures that duplicate emails are not allowed at the database level
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                CustomUserFactory(
                    email=test_users[0].email,
                    username=test_users[0].username,
                    first_name=test_users[0].first_name,
                    last_name=test_users[0].last_name,
                )
        for rec in CustomUser.objects.all_with_deleted():
            print(f'After factory attempt to create duplicate of record 0: {rec.email}: {rec.username}, {rec.deleted}')
        self.assertEqual(CustomUser.objects.all_with_deleted().count(), 4)
        self.assertEqual(CustomUser.objects.all_deleted().count(), 1)
        test_users[0].undelete()
        self.assertEqual(CustomUser.objects.all_with_deleted().count(), 4)
        self.assertEqual(CustomUser.objects.all_deleted().count(), 0)
        print(f'Restored: {test_users[0].email}: {test_users[0].username}, {test_users[0].deleted}')

    # To Do: test to make sure that undeleted users can still log into the system and function properly