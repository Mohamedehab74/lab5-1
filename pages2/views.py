from django.shortcuts import render, redirect
from .models import Login
from .forms import LoginForm

def home(request):
    return render(request, 'pages/home.html')

def form(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        data = Login(username=name, password=password)
        data.save()
        return redirect('home')  
        
    return render(request, 'pages/form.html', {'lf':LoginForm()})