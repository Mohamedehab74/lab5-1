from django.shortcuts import render
from .models import Login
from .forms import LoginForm

def home(request):
    return render(request, 'pages/home.html')
def form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():      
            form.save()

    return render(request, 'pages/form.html', {'lf':LoginForm()})
    

   