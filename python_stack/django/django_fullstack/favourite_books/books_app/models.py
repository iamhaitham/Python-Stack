from django.db import models
from login_registration_app.models import User

class BookManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData["book_description"])>0:
            if len(postData["book_description"])<5:
                errors["book_description"]="Description must be at least 5 characters"
        return errors

class Book(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True)
    uploaded_by=models.ForeignKey(User,related_name="uploaded_books",on_delete=models.CASCADE)
    favourites=models.ManyToManyField(User,related_name="favourite_books")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=BookManager()

def add_book(title,description,uploaded_by):
    user=User.objects.get(id=uploaded_by)
    return Book.objects.create(title=title,description=description,uploaded_by=user)

def display_all_books():
    return Book.objects.all()

def favourite_this_book(favourite_book_id,favourite_user_id):
    user=User.objects.get(id=favourite_user_id)
    book=Book.objects.get(id=favourite_book_id)
    return book.favourites.add(user)

def getBookIdByTitle(title):
    return Book.objects.get(title=title).id

def getBookById(book_id):
    return Book.objects.get(id=book_id)

def display_fav_books(user_id):
    user=User.objects.get(id=user_id)
    return user.favourite_books.all()

def unfavourite_this(user_id,book_id):
    user=User.objects.get(id=user_id)
    book=Book.objects.get(id=book_id)
    return user.favourite_books.remove(book)

def update_book(book_id,updated_book_title,update_book_description):
    book=Book.objects.get(id=book_id)
    book.title=updated_book_title
    book.description=update_book_description
    book.save()

def delete(book_id):
    print('im models in delete', '*'*15)
    book=Book.objects.get(id=book_id)
    book.delete()
    return True
    
    