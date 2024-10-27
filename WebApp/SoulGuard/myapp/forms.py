from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, Post, Survey

class SignUpForm(UserCreationForm):
    additional_details = forms.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        user_profile = UserProfile.objects.create(user=user, additional_details=self.cleaned_data['additional_details'])
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['question1_response', 'question2_response']

# forms.py



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
