from django.test import SimpleTestCase
from django.urls import reverse


class BookListSearchFilterTests(SimpleTestCase):
    def test_catalog_page_loads(self):
        response = self.client.get(reverse("book-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book Catalog")

    def test_title_search_filters_results(self):
        response = self.client.get(reverse("book-list"), {"q": "django"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django for Beginners")
        self.assertNotContains(response, "Clean Code")

    def test_category_filter_filters_results(self):
        response = self.client.get(reverse("book-list"), {"category": "Programming"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Crash Course")
        self.assertNotContains(response, "Clean Code")

    def test_empty_state_is_rendered(self):
        response = self.client.get(reverse("book-list"), {"q": "zzzz"})
        self.assertContains(response, "No books match your current search or category filter.")
