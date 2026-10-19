from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Import the Profile model from your accounts app
from accounts.models import Profile

@login_required(login_url='login')
def my_profile(request):
    user_profile = request.user.profile
    
    if request.method == 'POST':
        # Update basic user info
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()
        
        # Update profile specific fields
        user_profile.title = request.POST.get('title', '')
        
        # Only update skills if they are a freelancer
        if user_profile.role == 'freelancer':
            user_profile.skills = request.POST.get('skills', '')
            
        user_profile.save()
        messages.success(request, "Your profile has been successfully updated!")
        
        # Redirect back to the appropriate dashboard
        if user_profile.role == 'client':
            return redirect('client')
        return redirect('freelancer')

    return render(request, 'profile.html', {'profile': user_profile})