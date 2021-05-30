from django.shortcuts import render,redirect,HttpResponse
from . import models
from django.contrib import messages
from .models import Book

def root(request):
    context={
        "All_Books":models.display_all_books(),
        "fav_books":models.display_fav_books(request.session["id"]),
    }
    return render(request,"books.html",context)

def add_books(request):
    errors = Book.objects.validator(request.POST)
    if request.method=="POST":
        title=request.POST["book_title"]
        description=request.POST["book_description"]
        uploaded_by=request.session["id"]
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/books/")
        else:
            models.add_book(title,description,uploaded_by)
            favouriteThisBookId=models.getBookIdByTitle(title)
            models.favourite_this_book(favouriteThisBookId,uploaded_by)
            return redirect("/books")
    else:
        return HttpResponse("You are not allowed to manually modify the URL!")

def favourite_this(request,book_id):
        favourite_book_id=book_id
        favourite_user_id=request.session["id"]
        models.favourite_this_book(favourite_book_id,favourite_user_id)
        return redirect("/books/"+str(book_id))

def bookinfo(request,book_id):
    context={
    "A_Book":models.getBookById(book_id),
    "book_id":book_id,
    "fav_books":models.display_fav_books(request.session["id"]),
    }
    return render(request,"book_info.html",context)

def unfavourite_this(request,book_id):
    user_id=request.session["id"]
    models.unfavourite_this(user_id,book_id)
    return redirect("/books/"+str(book_id))

def update_book(request,book_id):
    errors = Book.objects.validator(request.POST)
    updated_book_title=request.POST["book_title"]
    update_book_description=request.POST["book_description"]
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/books/"+str(book_id))
    else:
        models.update_book(book_id,updated_book_title,update_book_description)
        return redirect("/books/"+str(book_id))

def delete(request,book_id):
    models.delete(book_id)
    return redirect("/books")
    