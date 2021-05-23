from django.shortcuts import render,HttpResponse,redirect
from . import models

def index(request):
    context={
        "All_Books":models.book_DB(),
    }
    return render(request,"index.html",context)

def add_book(request):
    if request.method=="POST":
        book_title=request.POST["book_title"]
        book_description=request.POST["book_description"]
        models.add_book(book_title,book_description)
        return redirect("/")
    else:
        return HttpResponse("You aren't allowed to manually adjust the URL!")

def books(request,number):
    context={
        "Some_Book":models.some_book(number),
        "All_Authors":models.all_authors(),
    }
    return render(request,"some_book.html",context)

def authors(request):
    context={
            "All_Authors":models.all_authors(),
        }
    return render(request,"authors.html",context)

def add_author(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        author_notes=request.POST["author_notes"]
        models.add_author(first_name=first_name,last_name=last_name,author_notes=author_notes)
        return redirect("/authors")
    else:
        return HttpResponse("You aren't allowed to manually adjust the URL!")  

def some_author(request,Num):
    context={
        "Some_Author":models.some_author(Num),
        "All_Books":models.book_DB(),
        "author_id":Num,
    }
    return render(request,"some_author.html",context)

def assign_book(request):
    if request.method=="POST":
        if request.POST["author_id"].isdigit()==True:
            author_id=request.POST["author_id"]
            assigned_book=request.POST["assigned_book"]
            models.assign_book(author_id,assigned_book)
            return redirect("/author/"+author_id)
        else:
           return HttpResponse("Only integers are allowed!")
    else:
        return HttpResponse("You aren't allowed to manually adjust the URL!")  

def some_book(request):
    if request.method=="POST":
        assigned_author=request.POST["assigned_author"]
        book_id=request.POST["book_id"]
        models.assignAuthor(assigned_author,book_id)
        return redirect("/books/"+book_id)
    else:
        return HttpResponse("You aren't allowed to manually adjust the URL!")