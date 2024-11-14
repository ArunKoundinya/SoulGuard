from django.contrib import admin
from .models import UserProfile, Post, Survey, Recommendation, UserActivity, SignInRecord

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Survey)
admin.site.register(Recommendation)
admin.site.register(UserActivity)
admin.site.register(SignInRecord)
