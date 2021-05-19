from django.shortcuts import render,redirect,HttpResponse
import random
import datetime

def index(request):
    if "gold" not in request.session:
        request.session["gold"]=0
    if "activity" not in request.session:
        request.session["activity"]=[]
    return render(request,"index.html")

def money(request):
    if request.method=="POST":
        if request.POST["hiddenInput"]=="Farm":
            request.session["gold"]+=random.randint(10,20)
            request.session["activity"].append(f"Earned {request.session['gold']} golds from the farm {datetime.datetime.now()}")
            request.session.save()
        elif request.POST["hiddenInput"]=="Cave":
            request.session["gold"]+=random.randint(5,10)
            request.session["activity"].append(f"Earned {request.session['gold']} golds from the cave {datetime.datetime.now()}" )
            request.session.save()
        elif request.POST["hiddenInput"]=="House":
            request.session["gold"]+=random.randint(2,5)
            request.session["activity"].append(f"Earned {request.session['gold']} golds from the house {datetime.datetime.now()}" )
            request.session.save()
        elif request.POST["hiddenInput"]=="Mall":
            x=random.randint(-50,50) # Because you may earn and you may lose gold, I started the randint from a negative value
            request.session["gold"]+=x
            print("_" * 30)
            print(x)
            if x<0:
                request.session["activity"].append(f"Entered a mall and lost {request.session['gold']} golds .. Ouch! {datetime.datetime.now()}")
                request.session.save()
            elif x>0:
                request.session["activity"].append(f"Entered a mall and earned {request.session['gold']} golds {datetime.datetime.now()}")
                request.session.save()
            elif x==0:
                request.session["activity"].append(f"Entered a mall and didn't spend any gold! {datetime.datetime.now()}")
                request.session.save()
        return redirect("/")
    else:
        return HttpResponse("Cheating is not allowed!")

def clear(request):
    request.session.clear()
    return redirect("/")

#For ninja bonus, I just have to delete the POST method
#and leave it in the default mode which is GET, and
#create routes for all places.
