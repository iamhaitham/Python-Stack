from django.shortcuts import render,HttpResponse,redirect
from . import models
from .models import User
from django.contrib import messages
import bcrypt


def root(request):
    if "id" not in request.session:
        return render(request,"index.html")
    else:
        return redirect("/books")


def success(request):
    if "id" in request.session:
        return redirect("/books")
    else:
        return redirect('/')
    

def registrationProcess(request):
    errors = User.objects.validator(request.POST)
    if request.method=="POST" :
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_pw=request.POST["confirm_password"]
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            if models.check_email(email=email)==False:
                hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
                user=models.register(first_name,last_name,email,hashed_pw)
                request.session["id"]=user.id
                request.session["FIRSTNAME"]=user.first_name
                request.session["LASTNAME"]=user.last_name
                request.session["EVENT"]="registered"
                return redirect("/success")

    else:
        return HttpResponse("You are not allowed to manually change the URL!")


def loginProcess(request):
    if request.method=="POST":
        username=request.POST["username"]
        userpw=request.POST["userpw"]
        user=models.login_username(username)
        if models.login_username_check(username)==False:
            if user and bcrypt.checkpw(userpw.encode(), user.password.encode()):
                request.session["id"]=models.get_user_id(username)
                request.session["FIRSTNAME"]=models.get_first_name(username)
                request.session["LASTNAME"]=models.get_last_name(username)
                request.session["EVENT"]="logged in"
                return redirect("/success")
            else:
                return HttpResponse("Log in information didn't match!")
        else:
            return HttpResponse("This email does not exist!")
    else:
        return HttpResponse("You are not allowed to manually change the URL!")


def logout(request):
    request.session.flush()
    return redirect("/")

