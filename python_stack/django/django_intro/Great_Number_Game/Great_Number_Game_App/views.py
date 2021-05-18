from django.shortcuts import render,HttpResponse,redirect
import random

# Create your views here.
def index(request):
    if "counter" not in request.session:
        request.session["counter"]=1
    else:
        request.session["counter"]+=1
    if "adminNumber" not in request.session:
        request.session["adminNumber"]=random.randint(1, 100)
        request.session["again"]="hidden"
        print(request.session["adminNumber"])
        return render(request,"index.html")
    else:
        return render(request,"index.html")
        

def check(request):
    if request.method=="POST":
        if request.POST["userNumber"].isdigit()==True:
            if int(request.POST["userNumber"])==request.session["adminNumber"]:
                request.session["style"]="won"
                request.session["content"]=f"{request.session['adminNumber']} was the number"
                request.session["attempts"]=f"You have attempted {request.session['counter']} times"
                request.session["again"]="submit"
                del request.session["adminNumber"]
                request.session["adminNumber"]=random.randint(1, 100)
                print(request.session["adminNumber"])
                return redirect("/")
            elif int(request.POST["userNumber"])>request.session["adminNumber"]:
                request.session["content"]="Too high!"
                request.session["style"]="high"
                request.session["again"]="hidden"
                return redirect("/")
            else:
                request.session["content"]="Too low!"
                request.session["style"]="low"
                request.session["again"]="hidden"
                return redirect("/")
        else:
            return HttpResponse("You are just allowed to enter intergers!")
    else:
        return HttpResponse("You aren't allowed to manually modify the URL!")

def again(request):
    if request.method=="POST":
        request.session["style"]="hiddenDIV"
        request.session["again"]="hidden"
        del request.session["content"]
        del request.session["attempts"]
        del request.session["counter"]
        return redirect("/")
    else:
        return HttpResponse("You aren't allowed to manually modify the URL!")