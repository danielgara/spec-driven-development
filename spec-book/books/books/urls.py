from django.urls import path

from books.views import BookDetailView, BookListView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<str:book_id>/", BookDetailView.as_view(), name="book-detail"),
]
