from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    # User
    def test_creates_user(self):
        # To create a user
        # create_user is called from MyUserManager
        user = User.objects.create_user('manno', 'manno@gmail.com', 'password@123')

        # Check if this user is instance of this User model
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'manno@gmail.com')


    # SuperUser
    def test_creates_super_user(self):
        user = User.objects.create_superuser('manno', 'manno@gmail.com', 'password@123')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'manno@gmail.com')


    # Error when no username passed
    def test_raises_error_when_no_username(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email='manno@gmail.com', password='password@123')

    def test_raises_error_message_when_no_username(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='manno@gmail.com', password='password@123')


    # Error when no email passed
    def test_raises_error_when_no_email(self):
        self.assertRaises(ValueError, User.objects.create_user, username='manno', email='', password='password@123')

    def test_raises_error_message_when_no_email(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='manno', email='', password='password@123')

    # With superuser status
    def test_creates_super_user_with_staff_status(self):
         with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='manno', email='manno@gmail.com', password='password@123', is_staff=False)

    def test_creates_super_user_with_superuser_status(self):
         with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='manno', email='manno@gmail.com', password='password@123', is_superuser=False)



