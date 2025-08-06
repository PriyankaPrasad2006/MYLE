from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    """Custom login view with better styling."""
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)


def signup_view(request):
    """User registration view."""
    if request.user.is_authenticated:
        return redirect('medicines:home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('auth:login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/signup.html', {'form': form})
