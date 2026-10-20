from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Pod, PodInvitation

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

@login_required(login_url='login')
def send_invitation(request):
    if request.method == 'POST':
        pod_id = request.POST.get('pod_id')
        username = request.POST.get('username')
        
        pod = get_object_or_404(Pod, id=pod_id)
        
        # Security: Only the captain can send invites
        if pod.captain != request.user:
            messages.error(request, "Only the Pod Captain can invite members.")
            return redirect('freelancer')
            
        try:
            freelancer = User.objects.get(username=username, profile__role='freelancer')
            
            # Prevent duplicate invites or inviting existing members
            if freelancer in pod.members.all():
                messages.warning(request, f"{username} is already in this Pod.")
            elif PodInvitation.objects.filter(pod=pod, freelancer=freelancer, status='pending').exists():
                messages.warning(request, f"An invitation is already pending for {username}.")
            else:
                PodInvitation.objects.create(pod=pod, freelancer=freelancer)
                messages.success(request, f"Invitation sent to {username}!")
        except User.DoesNotExist:
            messages.error(request, "Freelancer not found. Check the username.")
            
    return redirect('freelancer')

@login_required(login_url='login')
def respond_to_invitation(request, invite_id, action):
    invite = get_object_or_404(PodInvitation, id=invite_id, freelancer=request.user)
    
    if invite.status == 'pending':
        if action == 'accept':
            invite.status = 'accepted'
            invite.pod.members.add(request.user) # Add user to the Pod
            messages.success(request, f"You have joined {invite.pod.name}!")
        elif action == 'decline':
            invite.status = 'declined'
            messages.info(request, f"You declined the invite to {invite.pod.name}.")
        invite.save()
        
    return redirect('freelancer')