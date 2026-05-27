from django.views.generic import TemplateView

from books.services.book_service import filter_books, get_categories


class BookListView(TemplateView):
    template_name = "books/book_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q", "")
        category = self.request.GET.get("category", "")
        books = filter_books(query=query, category=category)
        context.update(
            {
                "books": books,
                "query": query,
                "selected_category": category,
                "categories": get_categories(),
            }
        )
        return context
