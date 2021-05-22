from django.shortcuts import render,HttpResponse,redirect
from . import models

def index(request):
    context={
    "All_Dojos":models.show_dojos(),
    }
    return render(request,"index.html",context)


def Dojo(request):
    if request.method=="POST":
        dojo_name=request.POST["name"]
        dojo_city=request.POST["city"]
        dojo_state=request.POST["state"]
        models.add_dojo(dojo_name,dojo_city,dojo_state)
        return redirect("/")
    else:
        return HttpResponse("You are not allowed to change the route manually!")


def Ninja(request):
    if request.method=="POST":
        ninja_first_name=request.POST["first_name"]
        ninja_last_name=request.POST["last_name"]
        ninja_select_dojo=request.POST["select_dojo"]
        models.add_ninja(ninja_select_dojo,ninja_first_name,ninja_last_name)
        return redirect("/")
    else:
        return HttpResponse("You are not allowed to change the route manually!")

def Delete(request):
    if request.method=="POST":
        ID=request.POST["deleteButton"]
        models.Delete(ID)
        return redirect("/")
    else:
        return HttpResponse("You are not allowed to change the route manually!")