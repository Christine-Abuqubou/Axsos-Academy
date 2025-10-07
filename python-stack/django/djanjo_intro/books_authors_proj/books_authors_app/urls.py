from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),               # Home page, shows all authors & books
    path('add_author/', views.add_author, name='add_author'),  # Add new author
    path('add_book/', views.add_book, name='add_book'),  
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]


