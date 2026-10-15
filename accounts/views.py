from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from . models import Profile
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def client(request):
    return render(request, 'client.html')

@login_required(login_url='login')
def freelancer(request):
    return render(request, 'freelancer.html')

def home(request):
    return render(request, 'home.html')

def logout(request):
    return render(request, 'login.html')


def find_freelancers(request):
    return render(request, 'freelancer.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = request.POST['role']

        if User.objects.filter(username = username).exists():
            messages.error(request, "User already exists")
            return redirect('signup')
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        user = User.objects.create_user(
            username = username,
            password = password
        )

        Profile.objects.create(
            user = user,
            role = role
        )

        user.save()

        messages.success(request, "Account created successfully")
        return redirect('login')
    
    return render(request, 'signup.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            login(request, user)
            
            role = user.profile.role

            if role == "client":
                return redirect('client')
            
            elif role == "freelancer":
                return redirect('freelancer')

        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')
        
    return render(request, 'login.html')      


    



# Create your views here.
