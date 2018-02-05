from django.urls import path
from . import views

app_name = 'creator'
urlpatterns = [
    path('<str:creatorname>/<int:content_pk>', views.creator_main, name="creator_page"),
    path('<str:creatorname>/', views.creator_main, name="creator_page"),

]
