from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.contrib.auth import login, logout
from .models import Custom_User
from django.contrib.auth.decorators import login_required

def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'account/registration.html', {'form': form})

def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.user.user_type == 'Job Seeker':
        print(request.user.user_type)
        return render(request, 'account/profile.html')
    
    elif request.user.user_type == 'Recruiter':
        return render(request, 'account/company_profile.html')
    else:
        return redirect('home')


def jobseeker_profile(request, pk):
    profile = Custom_User.objects.get(pk=pk).user_profile
    form = UserProfileForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            
            return redirect('profile')
        else:
            return HttpResponse(form.errors)
    return render(request, 'account/profile_update.html', {'form': form})


def company_profile(request, pk):
    profile = Custom_User.objects.get(pk=pk).user_compnay
    form = CompanyForm(instance=profile)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return HttpResponse(form.errors)
    return render(request, 'account/company_profile_update.html', {'form': form})





