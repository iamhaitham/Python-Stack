from django.shortcuts import render,HttpResponse,redirect
from . import models

# Create your views here.

def index(request):
    context={
    "db":models.show_db()
    }
    return render(request,"index.html",context)

def process(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        age=request.POST["age"]
        if age.isdigit()==True:
            models.add_to_db(first_name,last_name,email,age)
        else:
            return HttpResponse("Integers only!")
        return redirect("/")
    else:
        return HttpResponse("you can't change the route manually")

    