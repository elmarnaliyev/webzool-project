from django.shortcuts import render, redirect
from django.contrib import messages, auth
from main.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def index(request):
    return render(request, 'pages/index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')            
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':

        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is taken')
                return redirect('signup')
            else:
                # Looks good
                user = User.objects.create(email=email, first_name=first_name, last_name=last_name, phone=phone)
                user.set_password(password)
                user.save()
                messages.success(request, 'You are successfully registered')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        return redirect('signup')
    else:
        return render(request, 'signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are successfully logged out')
        return redirect('login')

def seo(request):
    return render(request, 'packages/seo.html')