from django.urls import path
from . import views

app_name = 'review'
urlpatterns = [
    path('<int:pk>/', views.board, name='review_board'),
    path('revise_review/<int:pk>', views.revise_review, name='revise_review'),
]
