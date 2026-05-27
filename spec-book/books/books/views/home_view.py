from django.views.generic import TemplateView

from books.services.book_service import get_featured_books


class HomeView(TemplateView):
    template_name = "books/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_books"] = get_featured_books()
        return context
