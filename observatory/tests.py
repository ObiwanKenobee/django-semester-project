from django.test import TestCase
from django.urls import reverse


class ObservatoryHomeTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('observatory:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Atlas Sanctum Observatory')
