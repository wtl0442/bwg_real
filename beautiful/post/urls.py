from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('write/', views.post_write, name='post_write'),
    path('tag/', views.show_tag, name='show_tag'),
    path('tag/<str:kwargs>/', views.tag_post_list, name='tag_post_list'),
]