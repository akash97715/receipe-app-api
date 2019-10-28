from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'akash97713@gmail.com'
        password = "Komlanknk9771"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'akash@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'Komlanknk9771')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'akash97715@gmail.com',
            'Akash1323'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
