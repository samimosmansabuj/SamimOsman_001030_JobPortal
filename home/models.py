from django.db import models
from authentication.models import Custom_User

class Job(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='user_job')
    title = models.CharField(max_length=500)
    number_of_openings = models.PositiveIntegerField()
    category = models.CharField(max_length=20)
    job_description = models.TextField()
    skills = models.CharField(max_length=100)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title


class Apply_Job(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='job_appy_user')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_appy')
    cover_later = models.TextField()
    resume = models.FileField(upload_to='user/resume/', blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.user} - {self.job}'

class Save_Job(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='job_save_user')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_save')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.user} - {self.job}'

