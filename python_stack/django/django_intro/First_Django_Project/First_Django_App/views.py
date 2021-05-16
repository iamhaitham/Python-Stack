from django.http.response import JsonResponse
from django.shortcuts import HttpResponse,redirect
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    return redirect("/blogs")

def json(request):
    return JsonResponse({"Title":"My first blog","content":"Lorem ipsum dolor sit, amet consectetur adipisicing elit."})
    