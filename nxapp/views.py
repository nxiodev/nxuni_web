from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import Newsletter
from django.contrib import messages
from .forms import NewsLetterForm

# from blog.models import blog

# Create your views here.
#coment

def home(request):
    # form = NewsLetterForm(request.POST)
    if request.method == "POST":
        email = request.POST['email'] 
        newsletter = Newsletter(email = email)
        newsletter.save()
        return render(request,"nxapp/home.html",{'email':email})
        # return HttpResponseRedirect("home")
    else:
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

