from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_details = models.CharField(max_length=255)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question1_response = models.BooleanField()
    question2_response = models.BooleanField()

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation_text = models.TextField()

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
