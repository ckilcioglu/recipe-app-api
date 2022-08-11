from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Should create a new user with and email successfully"""
        email = "caglar@gmail.com"
        password = "TestPassword123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """It should normalize email address for a new user"""
        email = "caglar@GMAil.cOm"
        password = "TestPassword123"
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """It should fail to create a user wih an invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123456')

    def test_create_new_superuser(self):
        """It should create a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
