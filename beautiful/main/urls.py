from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.showMain, name='showMain'),
    path('subscribeEmail', views.subscribe_email, name='subscribeEmail'),
    path('unsubscribeEmail', views.unsubscribe_email, name='unsubscribeEmail')
]
