from django.urls import path
from .views import for_you, to_whom_you_care, UserLoginView, dashboard, register, add_post, post_list, add_survey, home, terms_and_conditions

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('add_post/', add_post, name='add_post'),
    path('post_list/', post_list, name='post_list'),
    path('add_survey/', add_survey, name='add_survey'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('for_you/', for_you, name='for_you'),
    path('to_whom_you_care/', to_whom_you_care, name='to_whom_you_care'),
    path('terms-and-conditions/', terms_and_conditions, name='terms_and_conditions'),  # New path for Terms and Conditions
]
