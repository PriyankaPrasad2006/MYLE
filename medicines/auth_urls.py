from django.urls import path
from django.contrib.auth.views import LogoutView
from . import auth_views

app_name = 'auth'

urlpatterns = [
    path('login/', auth_views.CustomLoginView.as_view(), name='login'),
    path('signup/', auth_views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
