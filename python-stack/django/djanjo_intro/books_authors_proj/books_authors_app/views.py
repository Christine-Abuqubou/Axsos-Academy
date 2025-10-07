from django.shortcuts import render, redirect
from .models import Author, Book

def index(request):
    context = {
        "authors": Author.objects.all(),
        "books": Book.objects.all()
    }
    return render(request, "index.html", context)


def add_author(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST.get('notes', "")
        Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('/')



def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        author_id = request.POST['author_id']

    
        author = Author.objects.get(id=author_id)


        
        author.add_book(title, desc)

    return redirect('/')

def author_detail(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    if not author:
        return redirect('/')  # or handle error page

    # All books not yet associated with this author
    all_books = Book.objects.exclude(author=author)
    
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        if book_id:
            book = Book.objects.filter(id=book_id).first()
            if book:
                book.author = author
                book.save()
        return redirect('author_detail', author_id=author.id)
    
    context = {
        'author': author,
        'all_books': all_books
    }
    return render(request, 'author_detail.html', context)


# Book Detail
def book_detail(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    if not book:
        return redirect('/')  # or handle error page
    
    if request.method == "POST":
        author_id = request.POST.get('author_id')
        if author_id:
            author = Author.objects.filter(id=author_id).first()
            if author:
                book.author = author
                book.save()
        return redirect('book_detail', book_id=book.id)
    
    all_authors = Author.objects.exclude(id=book.author.id)
    
    context = {
        'book': book,
        'all_authors': all_authors
    }
    return render(request, 'book_detail.html', context)


