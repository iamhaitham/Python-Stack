from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,"index.html")

def result(request):
    if request.method=="POST":
        context={
            "name":request.POST['name'],
            "location":request.POST["location"],
            "language":request.POST["language"],
            "textarea":request.POST["textarea"],
        }
        return render(request,"result.html",context)   
    else:
        return HttpResponse("You can't access this URL!")

