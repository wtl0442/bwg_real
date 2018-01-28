from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

from beautiful import settings


def login(request):
    form = AuthenticationForm(request, request.POST or None)

    if request.method == "POST" and form.is_valid():
        auth_login(request, form.get_user())
        next = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
        return redirect(next)
    ctx = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', ctx)

def logout(request):
    if request.method == "POST":
        auth_logout(request)

    return redirect(reverse('accounts:login'))

# Create your views here.
