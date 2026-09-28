from django.db import models
from django.contrib.auth.models import User

class FreelancerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(upload_to='profile/',blank = True)
    bio = models.TextField()
    skills = models.CharField(max_length=100)
    experience = models.IntegerField()
    education = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    resume_upload = models.FileField(upload_to='resume/', blank= True) 


    def __str__ (self):
        return self.user.username

class ClientProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    company_name = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logo/', blank = True)
    company_desc = models.TextField()
    website = models.URLField(blank=True)
    location = models.CharField(max_length=20)

    def __str__ (self):
        return self.user.username



# Create your models here.
