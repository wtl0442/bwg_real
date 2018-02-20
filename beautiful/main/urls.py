from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.showMain, name='showMain'),
<<<<<<< HEAD

]
=======
    path('subscribeEmail', views.subscribe_email, name='subscribeEmail'),
    path('unsubscribeEmail', views.unsubscribe_email, name='unsubscribeEmail')
]
>>>>>>> 750cdebab184503ab58be307a4fd7b5645f10f53
