from django.shortcuts import render
from django.http import JsonResponse
from .forms import SubscribeForm
from .models import SubscribedEmail


def showMain(request):
    ctx = {
        'form': SubscribeForm()
    }
    return render(request, 'main/main.html', ctx)


def subscribe_email(request):
    form = SubscribeForm(request.POST)
    data = {
        'success': False,
    }
    if form.is_valid():
        email = form.cleaned_data['email']
        _email, created = SubscribedEmail.objects.get_or_create(email=email)
        data['success'] = True
        data['created'] = created

    return JsonResponse(data)


def unsubscribe_email(request):
    form = SubscribeForm(request.POST)
    data = {
        'success': False,
    }
    if form.is_valid():
        email = form.cleaned_data['email']
        deleted_count = SubscribedEmail.objects.filter(email=email).delete()[0]
        data['success'] = True
        data['deleted'] = bool(deleted_count)

    return JsonResponse(data)
