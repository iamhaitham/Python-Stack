from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    notes=models.TextField(null=True)
    books=models.ManyToManyField(Book,related_name="authors")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def book_DB():
    return Book.objects.all()

def add_book(book_title,book_description):
    return Book.objects.create(title=book_title,desc=book_description)

def some_book(number):
    return Book.objects.get(id=number)

def all_authors():
    return Author.objects.all()

def add_author(first_name,last_name,author_notes):
    return Author.objects.create(first_name=first_name,last_name=last_name,author_notes=author_notes)

def some_author(Num):
    return Author.objects.get(id=Num)

def assign_book(author_id,assigned_book):
    return Author.objects.get(id=author_id).books.add(assigned_book)

def assignAuthor(assigned_author,book_id):
    return Book.objects.get(id=book_id).authors.add(assigned_author)