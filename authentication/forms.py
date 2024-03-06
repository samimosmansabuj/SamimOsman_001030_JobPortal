from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import *

class UserRegistrationForm(UserCreationForm):
    USER_TYPE = (
        ('Job Seeker', 'Job Seeker'),
        ('Recruiter', 'Recruiter'),
    )
    
    display_name = forms.CharField(label='Display Name', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Display Name'}
    ))
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}
    ))
    email = forms.EmailField(label='Email Address', max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}
    ))
    password1 = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    password2 = forms.CharField(label='Confirm Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Password'}
    ))
    user_type = forms.CharField(label='User Type', required=True, max_length=20, widget=forms.Select(choices=USER_TYPE, attrs={'class': 'form-control'}))
    
    class Meta:
        model = Custom_User
        fields = ['display_name', 'username', 'email', 'user_type']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'phone_number', 'email', 'description', 'address', 'website']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['location', 'contact_number', 'skills', 'bio', 'resume', 'cover_later']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'cover_later': forms.Textarea(attrs={'class': 'form-control'}),
        }





