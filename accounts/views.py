from django.shortcuts import render, redirect
from functools import wraps
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile

def role_required(allowed_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Ensure the user is logged in and has a profile
            if request.user.is_authenticated and hasattr(request.user, 'profile'):
                # If they have the correct role, let them proceed
                if request.user.profile.role == allowed_role:
                    return view_func(request, *args, **kwargs)
                
                # If they snoop, show an error and bounce them back to their actual dashboard
                messages.warning(request, "Access denied. You have been redirected to your dashboard.")
                if request.user.profile.role == 'client':
                    return redirect('client')
                elif request.user.profile.role == 'freelancer':
                    return redirect('freelancer')
            
            # Fallback if something goes wrong
            return redirect('login')
        return wrapper
    return decorator


def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('signup')

        if not role:
            messages.error(request, 'Please select a role.')
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role=role)
        
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
        
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            try:
                if user.profile.role == 'client':
                    return redirect('client')
                elif user.profile.role == 'freelancer':
                    return redirect('freelancer')
            except Profile.DoesNotExist:
                messages.error(request, 'Profile data missing. Please contact support.')
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
            
    return render(request, 'login.html')

@login_required(login_url='login')
@role_required('client')
def client(request):
    return render(request, 'client.html')

@login_required(login_url='login')
@role_required('freelancer')
def freelancer(request):
    return render(request, 'freelancer.html')

@login_required(login_url='login')
@role_required('client')
def find_freelancers(request):
    freelancers = User.objects.filter(profile__role='freelancer')
    context = {
        'freelancers': freelancers
    }
    return render(request, 'find_freelancers.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
