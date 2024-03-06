from django import forms
from .models import Job, Apply_Job, Save_Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'number_of_openings', 'category', 'job_description', 'skills']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_openings': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Apply_Job
        fields = ['job', 'cover_later', 'resume']
        widgets = {
            'job': forms.Select(attrs={'class': 'form-control', 'readonly': True}),
            'cover_later': forms.Textarea(attrs={'class': 'form-control'}),
        }


