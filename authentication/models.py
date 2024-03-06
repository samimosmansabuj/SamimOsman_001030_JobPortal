from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Custom_User(AbstractUser):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Job Seeker', 'Job Seeker'),
        ('Recruiter', 'Recruiter'),
    )
    display_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=20, choices=USER_TYPE, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.username} | {self.email}'

@receiver(post_save, sender=Custom_User)
def create_user_profile_or_company(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'Recruiter':
            Company.objects.create(user=instance, email=instance.email)
        elif instance.user_type == 'Job Seeker':
            UserProfile.objects.create(user=instance)


class Company(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='user_compnay')
    company_name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(max_length=100)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Comapny Profile"


class UserProfile(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='user_profile')
    location = models.CharField(max_length=500, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    skills = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='user/resume/', blank=True, null=True)
    cover_later = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"




