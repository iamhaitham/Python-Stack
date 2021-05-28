from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib import messages
from .models import User
import bcrypt

def sign(request):
    return render(request,"index.html")


def success(request):
    if "id" in request.session:
        return render(request,"success.html")
    else:
        return redirect("/")


def wall(request):
    if "id" in request.session:
        context={
            "All_Messages":models.display_all_messages(),
        }
        return render(request,"wall.html",context)
    else:
        return HttpResponse("You can't access the wall without registering!")


def registrationProcess(request):
    errors = User.objects.validator(request.POST)
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_pw=request.POST["confirm_pw"]
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            if models.check_email(email)==False:
                user=models.create_user(first_name,last_name,email,pw_hash)
                request.session["id"]=user.id
                request.session["FIRSTNAME"]=user.first_name
                request.session["LASTNAME"]=user.last_name
                request.session["EVENT"]="registered"
                return redirect("/success")
            else:
                return HttpResponse("This email already exists") 
    else:
        return HttpResponse("You are not allowed to manually change the URL!")


def loginProcess(request):
    if request.method=="POST":
        username=request.POST["username"]        
        userpw=request.POST["userpw"]
        user=models.check_login(username)
        if user and bcrypt.checkpw(userpw.encode(), user.password.encode()):
            # myUser=models.get_user(username)
            request.session["id"]=user.id
            request.session["FIRSTNAME"]=user.first_name
            request.session["LASTNAME"]=user.last_name
            request.session["EVENT"]="logged in"
            return redirect("/success")
        else:
            return HttpResponse("Check login information")
    else:
        return HttpResponse("You are not allowed to manually change the URL!")


def message_process(request):
    if request.method=="POST":
        textarea=request.POST["textarea"]
        user_id=request.POST["user_id"]
        models.create_a_message(textarea,user_id)
        return redirect("/wall")
    else:
        return HttpResponse("You are not allowed to modify the URL manually!")


def logout(request):
    request.session.flush()
    return redirect("/")

def comment_process(request):
    if request.method=="POST":
        commentarea=request.POST["commentarea"]
        user_id=request.session["id"]
        msg_id=request.POST["msg_id"]
        models.create_a_comment(commentarea,user_id,msg_id)
        return redirect("/wall")
    else:
        return HttpResponse("You are not allowed to manually change the URL!")

def delete_process(request):
    if request.method=="POST":
        message_id=request.POST["messageID"]
        models.delete_a_post(message_id)
        return redirect("/wall") 
    else:
        return HttpResponse("You are not allowed to manually change the URL!")
