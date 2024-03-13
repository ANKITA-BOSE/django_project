from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from . forms import MyRegFrm

# Create your views here.

def about(request):
    return render(request, 'myapp/about.html')

def client(request):
    return render(request, 'myapp/client.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def index(request):
    return render(request, 'myapp/index.html')

def products(request):
    return render(request, 'myapp/products.html')

def userReg(request):
    if request.POST:
        form=MyRegFrm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registration is successful')
            except Exception :
                messages.error(request, 'Registration is unsuccessful')
    else:
        form=MyRegFrm()
    return render(request, 'myapp/reg.html',{'form':form})

 

 