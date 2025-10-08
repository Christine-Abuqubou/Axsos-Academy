from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("add_author/", views.add_author, name="add_author"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("authors/<int:author_id>/", views.author_detail, name="author_detail"),
]
