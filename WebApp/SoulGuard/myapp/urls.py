from django.urls import path
from .views import for_you, to_whom_you_care, UserLoginView, dashboard, register, add_post, post_list, add_survey, home
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('add_post/', views.add_post, name='add_post'),
    path('post_list/', views.post_list, name='post_list'),
    path('add_survey/', views.add_survey, name='add_survey'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('for_you/', for_you, name='for_you'),
    path('to_whom_you_care/', to_whom_you_care, name='to_whom_you_care'),
]
