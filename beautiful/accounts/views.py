from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, AdminPasswordChangeForm
from django.contrib import messages
from accounts.forms import SignupForm, ProfileForm, SkintypeForm
from accounts.models import Profile
from beautiful import settings
from social_django.models import UserSocialAuth




def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if request.method == "POST" and form.is_valid():
        return redirect(reverse('main:showMain'))
    ctx = {
        'form': form,
    }
    return render(request, 'accounts/login.html', ctx)


def logout(request):
    auth_logout(request)
    return redirect_previous_page(request)


def signup(request):
    signup_form = SignupForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse('main:showMain'))
    return render(request, 'accounts/signup.html', {
        'signup_form': signup_form,
        'profile_form': profile_form,
    })


def login_and_redirect_next(request, user):
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
    auth_login(request, user)
    next_url = request.GET.get('next') or settings.MAIN_REDIRECT_URL
    return redirect(next_url)


def redirect_previous_page(request):
    previous_page = request.META['HTTP_REFERER']
    return redirect(previous_page)


def profile_detail(request, username):
    ctx = {
        'profile': get_object_or_404(Profile, user__username=username)
    }
    return render(request, 'accounts/profile_detail.html', ctx)


@login_required
def update_profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.method == "POST" and form.is_valid():
        profile = form.save()
        return redirect(reverse('accounts:profile_detail', kwargs={
            'username': profile.user.username,
        }))
    ctx = {
        'form': form,
    }
    return render(request, 'accounts/edit_profile.html', ctx)


@login_required
def skin_type(request):
    form = SkintypeForm(request.POST or None, instance=request.user.profile)
    print('여기구나')
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('accounts:profile_detail', kwargs={
            'username': request.user.username,
        }))
    return render(request, 'accounts/skintype_test.html', {
        'form': form,
    })


def skin_type_test(request):
    return render(request, 'accounts/quiz.html')


@login_required
def settings(request):
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'accounts/settings.html', {
        'facebook_login': facebook_login,
        })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == "POST":
        form = PasswordForm(request.user, request.POST or None)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated')
            return redirect('main:showMain')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)

    return render(request, 'accounts/password.html', {'form': form})

