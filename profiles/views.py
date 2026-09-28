from django.shortcuts import render, redirect
from . models import ClientProfile
from . form import ClientProfileForm

def freelance_profile (request):
    return render(request, "freelancer_profile.html")

def client_profile (request):
    profile = ClientProfile.objects.filter(user=request.user).first()

    return render(request, "client_profile.html", {"profile":profile})

def edit_profile (request):
    profile = ClientProfile.objects.filter(user=request.user).first()
    if profile is None:
        profile = ClientProfile(user=request.user)

    if request.method == "POST":
        form = ClientProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect("client_profile")
        
    else:
        form = ClientProfileForm(instance=profile)

    return render(request, "edit_profile.html",{"form":form})
