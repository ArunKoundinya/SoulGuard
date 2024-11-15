import sys
import os
# Add the path to the jupyternotebooks folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from django.shortcuts import render, redirect
from .forms import SignUpForm, PostForm, SurveyForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Recommendation, Survey, UserProfile, Post
from django.contrib.auth.views import LoginView
from datetime import datetime
import os
import sys

import jupyternotebooks.mainpredictions¸

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        birthdate = request.POST.get('birthdate')
        
        # Check if birthdate is provided and calculate age
        if birthdate:
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
            age = (datetime.now() - birthdate).days // 365
            if age < 18:
                messages.error(request, 'You must be at least 18 years old to register.')
                return render(request, 'myapp/register.html', {'form': form})

        if form.is_valid():
            user = form.save()
            # Create user profile without additional details
            UserProfile.objects.get_or_create(user=user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'myapp/register.html', {'form': form})

def add_post(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to post.")
        return redirect('login')  # Ensure you have a login URL

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            post_text = post.content

            recommendation = jupyternotebooks.mainpredictions.finalpredictions(post_text)
            
            messages.success(request, 'Post added successfully')
            
            return render(request, 'myapp/recommendation.html',{'recommendation': recommendation})
            #return redirect('post_list')
        else:
            messages.error(request, form.errors)
    else:
        form = PostForm()
    return render(request, 'myapp/add_post.html', {'form': form})

def add_survey(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to submit surveys.")
        return redirect('login')

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.user = request.user
            survey.save()
            messages.success(request, 'Survey submitted successfully')
            return redirect('survey_results')
        else:
            messages.error(request, form.errors)
    else:
        form = SurveyForm()
    return render(request, 'myapp/add_survey.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'myapp/post_list.html', {'posts': posts})

def home(request):
    return render(request, 'myapp/home.html')

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'myapp/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/add_post/'

def dashboard(request):
    activities = UserActivity.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'myapp/dashboard.html', {'activities': activities})

def for_you(request):
    return render(request, 'myapp/for_you.html')

def to_whom_you_care(request):
    return render(request, 'myapp/to_whom_you_care.html')

def terms_and_conditions(request):
    return render(request, 'myapp/terms_and_conditions.html')
