from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_homepage_loads_and_shows_featured_heading(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Featured Books")

    def test_homepage_only_shows_featured_books(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Django for Beginners")
        self.assertNotContains(response, "Clean Code")
