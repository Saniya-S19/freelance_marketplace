from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pods.models import Pod
from .models import Pitch

@login_required(login_url='login')
def create_pitch(request):
    if request.method == 'POST':
        # 1. Grab the hidden target data from the form
        target_type = request.POST.get('target_type')
        target_id = request.POST.get('target_id')
        
        # 2. Grab the project details
        title = request.POST.get('project_title')
        description = request.POST.get('description')
        budget = request.POST.get('budget')

        # 3. Initialize the pitch
        pitch = Pitch(
            client=request.user,
            project_title=title,
            description=description,
            budget=budget
        )

        # 4. Attach it to the correct target
        if target_type == 'freelancer':
            freelancer = User.objects.get(id=target_id)
            pitch.freelancer = freelancer
            target_name = freelancer.username
        elif target_type == 'pod':
            pod = Pod.objects.get(id=target_id)
            pitch.pod = pod
            target_name = pod.name
        
        pitch.save()
        messages.success(request, f"Your pitch for '{title}' was sent to {target_name}!")
        return redirect('find_freelancers')
        
    return redirect('find_freelancers')