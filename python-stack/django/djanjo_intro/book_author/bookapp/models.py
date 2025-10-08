from django.db import models

class Author (models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200 )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def add_author(first_name, last_name, notes):
        return Author.objects.create(
            first_name=first_name,
            last_name=last_name,
            notes=notes
        )
    


class Book(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    updated_at=models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author, related_name="books")
    
    def add_book(title, desc):
        return Book.objects.create(title=title, desc=desc)

    
    
    
    

# Create your models here.
