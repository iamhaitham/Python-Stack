from django.shortcuts import render, HttpResponse,redirect
import datetime




# Create your views here.
def root(request):
    return redirect("/time_display")

def index(request):
    x = datetime.datetime.now()
    context={
        "dt":x,
    }
    return render(request,'index.html',context)
