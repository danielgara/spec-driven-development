from django.test import SimpleTestCase
from django.urls import reverse


class BookDetailTests(SimpleTestCase):
    def test_detail_page_loads_for_valid_book(self):
        response = self.client.get(reverse("book-detail", kwargs={"book_id": "b1"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django for Beginners")

    def test_detail_returns_404_for_invalid_book(self):
        response = self.client.get(reverse("book-detail", kwargs={"book_id": "unknown"}))
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Book not found", status_code=404)
