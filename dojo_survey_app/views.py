from django.shortcuts import render

def index(request):
    return render(request, "form.html")

def formsubmit(request):
    if request.method == "POST":
        things = {
            "name": request.POST["name"],
            "location": request.POST["location"],
            "favlang": request.POST["favlang"],
            "comments": request.POST["comments"],
        }
        return render(request, "results.html", things)

# Create your views here.
