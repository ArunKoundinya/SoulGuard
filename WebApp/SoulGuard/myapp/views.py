from django.shortcuts import render, redirect
from .forms import SignUpForm, PostForm, SurveyForm ,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Recommendation, Survey, UserProfile,Post
from django.contrib.auth.views import LoginView


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Check if UserProfile already exists to avoid duplication
            UserProfile.objects.get_or_create(user=user, defaults={'additional_details': form.cleaned_data.get('additional_details', '')})
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
            messages.success(request, 'Post added successfully')
            return redirect('post_list')
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
        return self.get_redirect_url() or '/'

# views.py
from django.shortcuts import render
from .models import UserActivity

def dashboard(request):
    activities = UserActivity.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'myapp/dashboard.html', {'activities': activities})

# views.py

from django.shortcuts import render

def for_you(request):
    return render(request, 'myapp/for_you.html')

def to_whom_you_care(request):
    return render(request, 'myapp/to_whom_you_care.html')
