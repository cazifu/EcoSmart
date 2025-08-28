from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


from App.forms import RegisterForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render('auth/register.html')
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        print()
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            return redirect('login')
    return render(request, 'auth/login.html')

def register(request):
    register = RegisterForm(request.POST)
    if request.method == 'POST':
        
        if register.is_valid():
            register.save
            return render(request, 'home.html')
        else:
            print('no')   
            errores = register.errors    
            return render(request, 'auth/register.html',{'registerForm' : register, 'errores': errores})

def header(request):
    return render(request, 'header.html')