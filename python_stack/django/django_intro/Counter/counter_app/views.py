from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def index(request):
    print(request.session)
    if "counter" not in request.session:
        request.session["counter"]=0
    else:
        request.session["counter"]+=1

    if "actualcounter" not in request.session:
        request.session["actualcounter"]=0
    else:
        request.session["actualcounter"]+=1
    return render(request,"index.html")

def destroy(request):
    del request.session["counter"]
    return redirect("/")

def increment_by_2(request):
    #everytime the page refreshes it will add 1, so this button will just add 1. Thus, the total increment will be 2.
    request.session["counter"]+=1
    return redirect("/")

def choose_increment_value(request):
    # .isdigit() method checks whether the value is a number or, for example, a mixed characters or even an empty value
    if request.GET["choose"].isdigit()==False:
        # I don't want to change neither the counter nor the actual counter if the user don't enter a number
        request.session["counter"]-=1
        request.session["actualcounter"]-=1
        return redirect("/")
    else:
        request.session["counter"]+=int(request.GET["choose"])-1
        return redirect("/")
