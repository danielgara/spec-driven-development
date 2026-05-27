from django.http import Http404
from django.views.generic import TemplateView

from books.services.book_service import get_book_by_id


class BookDetailView(TemplateView):
    template_name = "books/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get("book_id")
        book = get_book_by_id(book_id)
        if book is None:
            raise Http404("Book not found")
        context["book"] = book
        return context
