from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_view(request):
    """Login view for the for the user."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user

            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse('learning_logs:index'))


    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout_view(request):
    #if request.method == 'POST':
        # Log the user out
        logout(request)
        return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Register a new user."""
    if request.method == 'POST':
        # Display blank registration form.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Log the user in.
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    else:
        # Process completed form.
        form = UserCreationForm()
    context = {'form' :form}
    return render(request, 'users/register.html', context)
