from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pod

@login_required(login_url='login')
def create_pod(request):
    if request.method == 'POST':
        name = request.POST.get('pod_name')
        description = request.POST.get('pod_description')

        # Prevent duplicate names
        if Pod.objects.filter(name=name).exists():
            messages.error(request, "A Pod with this name already exists. Please choose another.")
            return redirect('freelancer')

        # Create the Pod and assign the captain
        new_pod = Pod.objects.create(
            name=name,
            description=description,
            captain=request.user
        )
        
        # Add the captain as the first member of the ManyToMany field
        new_pod.members.add(request.user)

        messages.success(request, f"Pod '{name}' has been deployed successfully!")
        return redirect('freelancer')
        
    return redirect('freelancer')