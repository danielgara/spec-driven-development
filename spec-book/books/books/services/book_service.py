"""Read-only query helpers for file-backed book data."""

from books.data.books_data import BOOKS


def get_all_books():
    return list(BOOKS)


def get_book_by_id(book_id):
    for book in BOOKS:
        if str(book.get("id")) == str(book_id):
            return book
    return None


def get_categories():
    categories = {book.get("category", "").strip() for book in BOOKS if book.get("category")}
    return sorted(categories)


def get_featured_books():
    return [book for book in BOOKS if book.get("featured") is True]


def filter_books(query="", category=""):
    normalized_query = (query or "").strip().lower()
    normalized_category = (category or "").strip().lower()

    filtered = get_all_books()
    if normalized_query:
        filtered = [
            book for book in filtered if normalized_query in book.get("title", "").lower()
        ]
    if normalized_category:
        filtered = [
            book for book in filtered if book.get("category", "").strip().lower() == normalized_category
        ]

    return filtered
