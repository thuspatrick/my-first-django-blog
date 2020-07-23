from django.shortcuts import render

def home(request):
    print(request.user)
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})