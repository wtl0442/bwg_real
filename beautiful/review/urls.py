from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('load_more_reivew/', views.load_more_review, name='dummy'),
    path('load_more_reivew/<int:review_count>', views.load_more_review, name='load_more_review'),
]


# the url named 'dummy' is just for the reverse for 'review_list.html'