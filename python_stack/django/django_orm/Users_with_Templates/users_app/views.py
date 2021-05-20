from django.shortcuts import render,redirect,HttpResponse
from . import models

# Create your views here.
def index(request):
    context = {
        "show_all_the_records": models.show_db(),
    }
    return render(request,"index.html",context)

def process(request):
    if request.method=="POST":
        request.session["first_name"]=request.POST["first_name"]
        request.session["last_name"]=request.POST["last_name"]
        request.session["email"]=request.POST["email"]
        if request.POST["age"].isdigit():
            request.session["age"]=int(request.POST["age"])
            models.add_to_db(request.session["first_name"],request.session["last_name"],request.session["email"],request.session["age"])
            return redirect("/")
        else:
            return HttpResponse("Age is just an integer!")
    else:
        return HttpResponse("You are not allowed to manually adjust the URL!")
