from django.contrib import admin
from .models import UserProfile, Post, Survey, Recommendation

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Survey)
admin.site.register(Recommendation)
