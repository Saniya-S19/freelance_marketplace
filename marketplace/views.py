from django.shortcuts import redirect, get_object_or_404
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

@login_required(login_url='login')
def update_pitch_status(request, pitch_id):
    if request.method == 'POST':
        pitch = get_object_or_404(Pitch, id=pitch_id)
        new_status = request.POST.get('status') # Will be 'accepted' or 'declined'
        
        # Security: Verify the user has permission to answer this pitch
        is_authorized = False
        if pitch.freelancer == request.user:
            is_authorized = True
        elif pitch.pod and request.user in pitch.pod.members.all():
            is_authorized = True
            
        if is_authorized and new_status in ['accepted', 'declined']:
            pitch.status = new_status
            pitch.save()
            messages.success(request, f"You have {new_status} the pitch: '{pitch.project_title}'")
        else:
            messages.error(request, "You are not authorized to update this pitch.")
            
    return redirect('freelancer')