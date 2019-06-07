from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Testing that user creation using email is working"""
        email = 'test@mail.com'
        password = 'pass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        """Testing that the email for the new user is normalized"""
        email = 'test@MAIL.COM'
        password = 'pass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password="123")

    def test_create_new_superuser(self):
        """"Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@mail.co', '123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
