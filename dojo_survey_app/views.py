from django.shortcuts import render, redirect

def index(request):
    return render(request, "form.html")

def formdata(request):
        name = request.POST["name"]
        location = request.POST["location"]
        favlang = request.POST["favlang"]
        comments = request.POST["comments"]
        return redirect('/')

def formsubmit(request):
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['favlang'] = request.POST['favlang']
        request.session['comments'] = request.POST['comments']
        return render(request, "results.html")

# Create your views here.
