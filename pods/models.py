from django.db import models
from django.contrib.auth.models import User

class Pod(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(
        help_text="Describe the Pod's specialty (e.g., 'Full-Stack Web3 Launch Squad')"
    )
    
    captain = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='captain_of_pods'
    )
    
    members = models.ManyToManyField(
        User, 
        related_name='joined_pods'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class PodInvitation(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    )
    
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE, related_name='invitations')
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pod_invitations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Invite to {self.freelancer.username} for {self.pod.name}"