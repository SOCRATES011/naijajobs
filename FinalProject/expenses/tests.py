from django.test import SimpleTestCase
from django.urls import reverse


class AuthRouteTests(SimpleTestCase):
    def test_login_route_exists(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
