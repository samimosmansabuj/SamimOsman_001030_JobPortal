from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    
    path('add-job/', add_job, name='add_job'),
    path('delete-job/<int:pk>/', delete_job, name='delete_job'),
    path('job-post-list/', job_post_list, name='job_post_list'),
    path('matching-job/', job_list, name='job_list'),
    
    path('apply-job/', apply_job_list, name='apply_job_list'),
    path('cancel-job/<int:pk>/', applied_cancel, name='applied_cancel'),
    path('apply/<int:pk>/', apply_job, name='apply_job'),
]