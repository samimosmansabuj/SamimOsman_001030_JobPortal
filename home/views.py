from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import *
from .models import *

def home(request):
    context = {}
    if request.user.is_authenticated:
        if request.user.user_type=='Job Seeker':
            user = request.user.job_appy_user.all()
            print(user)
            applied_job = Apply_Job.objects.filter(user=request.user)
            context['applied_job'] = applied_job
    job = Job.objects.all()
    context['job'] = job
    return render(request, 'home/home.html', context)

@login_required
def applied_cancel(request, pk):
    applied_job = get_object_or_404(Apply_Job, pk=pk)
    applied_job.delete()
    return redirect('apply_job_list')


def search(request):
    search_key = request.GET.get('search_key')
    print(search_key)
    job = Job.objects.filter(
        Q(title__icontains=search_key) |
        Q(number_of_openings__icontains=search_key) |
        Q(category__icontains=search_key) |
        Q(job_description__icontains=search_key) |
        Q(skills__icontains=search_key) |
        Q(created_date__icontains=search_key) |
        Q(updated_date__icontains=search_key)
    )
    return render(request, 'home/search.html', {'job': job})
    

@login_required
def add_job(request):
    if request.user.user_type == 'Recruiter':
        form = JobForm()
        if request.method =='POST':
            form = JobForm(request.POST)
            if form.is_valid():
                job = form.save(commit=False)
                job.user = request.user
                job.save()
                return redirect('home')
        return render(request, 'job/add_job.html', {'form': form})
    else:
        return redirect('job_list')


def job_list(request):
    try:
        user = request.user
        skils = user.user_profile.skills
        
        job = Job.objects.filter(
            Q(title__icontains=skils) |
            Q(number_of_openings__icontains=skils) |
            Q(category__icontains=skils) |
            Q(job_description__icontains=skils) |
            Q(skills__icontains=skils) |
            Q(created_date__icontains=skils) |
            Q(updated_date__icontains=skils)
        )
        return render(request, 'job/job_list.html', {'job': job})
    except:
        return redirect('home')

@login_required
def apply_job(request, pk):
    if request.user.user_type == 'Job Seeker':
        job = get_object_or_404(Job, pk=pk)
        form = ApplyJobForm(initial={'job': job})
        
        if request.method == 'POST':
            form = ApplyJobForm(request.POST, initial={'job': job})
            if form.is_valid():
                job_apply = form.save(commit=False)
                job_apply.user = request.user
                job_apply.save()
                return redirect('job_list')
        
        return render(request, 'job/job_apply.html', {'job': job, 'form': form})
    else:
        return redirect('profile')

@login_required
def apply_job_list(request):
    job = Apply_Job.objects.filter(user=request.user)
    return render(request, 'job/apply_job_list.html', {'job': job})

@login_required
def job_post_list(request):
    if request.user.user_type == 'Recruiter':
        user = request.user
        job = Job.objects.filter(user=user)
        return render(request, 'job/post_job_list.html', {'job': job})
    else:
        return redirect('home')

@login_required
def delete_job(request, pk):
    if request.user.user_type == 'Recruiter':
        job = get_object_or_404(Job, pk=pk)
        job.delete()
        return redirect('job_post_list')
    else:
        return redirect('home')

