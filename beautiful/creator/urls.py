from django.urls import path
from . import views

app_name = 'creator'
urlpatterns = [
    path('', views.creator_main, name="creator_page_main"),
    path('review_board/<int:item_pk>/', views.review_board, name='review_board'),
    path('create_review/<int:item_pk>/', views.create_review, name='create_review'),
    path('delete_review/<int:review_pk>/', views.delete_review, name='delete_review'),
    path('<str:creatorname>/', views.creator_main, name="creator_page"),
    path('<str:creatorname>/<int:content_pk>/', views.creator_main, name="creator_page"),
]
