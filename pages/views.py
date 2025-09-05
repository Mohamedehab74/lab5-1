from django.shortcuts import render
from .models import Login

def home(request):
    return render(request, 'pages/home.html')

def form(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')  

        if username and password: 
            data = Login(username=username, password=password)  
            data.save()  
            message = "Login Success"
        else:
            message = "Both fields are required"

    return render(request, 'pages/form.html',{"message" : message})