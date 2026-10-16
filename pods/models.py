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