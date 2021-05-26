from django.shortcuts import render,HttpResponse,redirect
from . import models
from .models import User, UserManager
from django.contrib import messages
import bcrypt
import datetime

def root(request):
    return render(request,"index.html")


def success(request):
    if "id" in request.session:
        return render(request,"success.html")
    else:
        return redirect('/')
    

def registrationProcess(request):
    errors = User.objects.validator(request.POST)
    if request.method=="POST" :
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_pw=request.POST["confirm_pw"]
        birthday=request.POST["date"]
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            if models.check_email(email=email)==False:
                hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
                user=models.register(first_name,last_name,email,hashed_pw,birthday)
                request.session["id"]=user.id
                request.session["FIRSTNAME"]=user.first_name
                request.session["LASTNAME"]=user.last_name
                request.session["EVENT"]="registered"
    else:
        return HttpResponse("You are not allowed to manually change the URL!")

def loginProcess(request):
    if request.method=="POST":
        username=request.POST["username"]
        userpw=request.POST["userpw"]
        user=models.login_username(username)
        if user and bcrypt.checkpw(userpw.encode(), user.password.encode()):
            request.session["id"]=models.get_user_id(username)
            request.session["FIRSTNAME"]=models.get_first_name(username)
            request.session["LASTNAME"]=models.get_last_name(username)
            request.session["EVENT"]="logged in"
            return redirect("/success")
        else:
            return HttpResponse("Log in information didn't match!")
    else:
        return HttpResponse("You are not allowed to manually change the URL!")

def logout(request):
    request.session.flush()
    return redirect("/")

