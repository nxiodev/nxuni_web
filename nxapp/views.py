from django.shortcuts import render, HttpResponse
# from blog.models import blog

# Create your views here.

def home(request):
    return render(request, 'nxapp/home.html')

def portfolios(request):
    return render(request, 'nxapp/strategies.html')

def servicios(request):
    return render(request, 'nxapp/consultoria.html')

def blog(request):
    return render(request, 'nxapp/blog.html')

def smartdapps(request):
    return render(request, 'nxapp/smartdapps.html')

def nxbot(request):
    return render(request, 'nxapp/nxbot.html')

def contacto(request):
    return render(request, 'nxapp/contactus.html')