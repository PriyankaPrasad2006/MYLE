from django.urls import path
from . import auth_views

app_name = 'auth'

urlpatterns = [
    path('login/', auth_views.CustomLoginView.as_view(), name='login'),
    path('signup/', auth_views.signup_view, name='signup'),
    path('logout/', auth_views.CustomLogoutView.as_view(), name='logout'),
]
