from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile, Post, Survey
from datetime import date

class SignUpForm(UserCreationForm):
    birthdate = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Birthdate"
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'birthdate')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  # Ensure 'content' is included
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your post here...',
                'rows': 4,
                'maxlength': 500,
            }),
        }
        labels = {
            'content': 'Your Post',
        }

class SurveyForm(forms.Form):
    QUESTION_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    
    # Define two questions with Yes/No options
    question_1 = forms.ChoiceField(choices=QUESTION_CHOICES, widget=forms.RadioSelect, label="Are you very frustrated today?")
    question_2 = forms.ChoiceField(choices=QUESTION_CHOICES, widget=forms.RadioSelect, label="Do you feel entire weight on your shoulders?")

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
