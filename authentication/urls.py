from django.urls import path
from .views import *


urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', registration, name='registration'),
    
    path('profile/', profile, name='profile'),
    path('jobseeker-profile/<int:pk>/', jobseeker_profile, name='jobseeker_profile'),
    path('company-profile/<int:pk>/', company_profile, name='company_profile'),
    
]