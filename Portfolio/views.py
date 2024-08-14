from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'Portfolio/index.html')

def About(request):
    
    return render(request,'Portfolio//about.html')


def Contact(request):
    
    return render(request,'Portfolio//contact.html')

def Services(request):
    
    return render(request,'Portfolio//services.html')

def Portfolio(request):
    
    return render(request,'Porfolio//work.html')