from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import SignupForm, ProfileForm, SkintypeForm
from accounts.models import Profile
from beautiful import settings


def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if request.method == "POST" and form.is_valid():
        return login_and_redirect_next(request, form.get_user())
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


def skin_type(request):
    if request.user.is_authenticated:
        form = SkintypeForm(request.POST or None, instance=request.user.profile)
        if request.method == "POST" and form.is_valid():
            form.save()

            if request.user.profile.skin_type == '건성피부(민감성피부)':
                skin_type_name = 'dry'
            elif request.user.profile.skin_type == '중성(약한 민감성 피부)':
                skin_type_name = 'neutral'
            elif request.user.profile.skin_type == '복합성 피부':
                skin_type_name = 'complex'
            elif request.user.profile.skin_type == '지성피부':
                skin_type_name = 'oily'
            else:
                skin_type_name = 'unresolved'
            return redirect(reverse('accounts:skin_type_result', kwargs={
                'type': skin_type_name,
            }))
        return render(request, 'accounts/skintype_test.html', {
            'form': form,
        })
    else:
        form = SkintypeForm(request.POST or None)
        return render(request, 'accounts/skintype_test.html', {
            'form': form,
        })


def skin_type_test(request):
    return render(request, 'accounts/quiz.html')


def skin_type_result(request, type):
    if type == 'dry':
        return render(request, 'skintype/dry_skin.html')
    elif type == 'neutral':
        return render(request, 'skintype/neutral_skin.html')
    elif type == 'complex':
        return render(request, 'skintype/complex_skin.html')
    elif type == 'oily':
        return render(request, 'skintype/oily_skin.html')
    elif type == 'unresolved':
        return render(request, 'skintype/unresolved_skin.html')