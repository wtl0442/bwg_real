from django.urls import path
from . import views

app_name = 'creator'
urlpatterns = [
    path('main/', views.creator_main, name="creator_main"),
]
