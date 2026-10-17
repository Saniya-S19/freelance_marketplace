from django.db import models
from django.contrib.auth.models import User
from pods.models import Pod

class Pitch(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    )

    # The Client sending the pitch
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_pitches')
    
    # The Target: EITHER a solo freelancer OR a Pod
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_pitches', null=True, blank=True)
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE, related_name='received_pitches', null=True, blank=True)
    
    # Project Details
    project_title = models.CharField(max_length=200)
    description = models.TextField(help_text="Describe the project scope, deliverables, and timeline.")
    budget = models.DecimalField(max_digits=10, decimal_places=2, help_text="Proposed budget")
    
    # Pitch Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        target = self.pod.name if self.pod else self.freelancer.username
        return f"{self.project_title} - pitched to {target}"