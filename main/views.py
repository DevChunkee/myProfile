from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def experience(request):
    return render(request, 'main/experience.html')

def projects(request):
    return render(request, 'main/projects.html')

def contacts(request):
    return render(request, 'main/contacts.html')