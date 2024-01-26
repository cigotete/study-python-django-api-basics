from django.urls import path
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView

urlpatterns = [
    path("author", AuthorListView.as_view(), name="author_list"),
    path("author/<int:pk>", AuthorDetailView.as_view(), name="author_detail"),
    path("book", BookListView.as_view(), name="book_list"),
    path("book/<int:pk>", BookDetailView.as_view(), name="book_detail"),
]