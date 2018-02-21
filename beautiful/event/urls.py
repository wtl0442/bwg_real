from django.urls import path
from . import views
app_name = 'event'

urlpatterns = [
    path('tag/<int:tag_pk>/', views.event_main, name='event_main_by_tag'),
    path('main/', views.event_main, name='event_main'),
    path('create/', views.event_create, name='event_create'),
    path('place/', views.event_place, name='event_place'),



]