from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book

def index(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
    }
    return render(request, "index.html", context)


def add_book(request):
    if request.method == "POST":
        Book.add_book(
            title=request.POST["title"],
            desc=request.POST["desc"]
        )
    return redirect("index")


def add_author(request):
    if request.method == "POST":
        Author.add_author(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            notes=request.POST.get("notes","") 
        )
    return redirect("index")


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    available_authors = Author.objects.exclude(id__in=book.authors.all())

    if request.method == "POST":
        author_id = request.POST.get("author_id")
        if author_id:
            book.add_author_to_book(author_id)
        return redirect("book_detail", book_id=book.id)

    context = {
        "book": book,
        "available_authors": available_authors,
    }
    return render(request, "book_detail.html", context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    available_books = Book.objects.exclude(id__in=author.books.all())

    if request.method == "POST":
        book_id = request.POST.get("book_id")
        if book_id:
            author.add_book_to_author(book_id)
        return redirect("author_detail", author_id=author.id)

    context = {
        "author": author,
        "available_books": available_books,
    }
    return render(request, "author_detail.html", context)
