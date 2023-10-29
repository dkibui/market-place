from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='Andrew', email="andrew@email.com", password="TestPassword@12")

        self.assertEqual(user.username, "Andrew")
        self.assertEqual(user.email, "andrew@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username="admin1", email="admin1@email.com",
                                                   password="TestPassword@1234")

        self.assertEqual(admin_user.username, "admin1")
        self.assertEqual(admin_user.email, "admin1@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
