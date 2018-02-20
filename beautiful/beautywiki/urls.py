from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    path('', views.wikimain, name='wikimain'),
    path('trouble/', views.trouble_wiki, name='trouble_wiki'),
]