from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.forms import UserCreationForm
from django.dispatch import receiver

import logging

logger = logging.getLogger(__name__)


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)
            return redirect('polls')
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def get_client_ip(request):
    """Get the visitor’s IP address using request headers."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


logger = logging.getLogger("mysite")


@receiver(user_logged_in)
def login_log(request, user, **kwargs):
    """loggin in logger."""
    user_ip = get_client_ip(request)
    logger.info(f"{user.username} logged in from {user_ip}")


@receiver(user_login_failed)
def unsuccess_login_log(request, user, **kwargs):
    """Unsuccessful login logger."""
    user_ip = get_client_ip(request)
    logger.warning(
        f"Invalid login for {user.username} with IP address: {user_ip}")


@receiver(user_logged_out)
def logout_log(request, user, **kwargs):
    """loggin out logger."""
    user_ip = get_client_ip(request)
    logger.info(f"{user.username} with IP address: {user_ip} has logged out.")
