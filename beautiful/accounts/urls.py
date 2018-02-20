<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path

>>>>>>> 750cdebab184503ab58be307a4fd7b5645f10f53
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('skintype_test/', views.skin_type_test, name='skin_type_test'),
    path('skintype_test/skintype/', views.skin_type, name='skin_type'),
    path('skintype_test/skintype/<str:type>', views.skin_type_result, name='skin_type_result'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
<<<<<<< HEAD

    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),



]


=======
]
>>>>>>> 750cdebab184503ab58be307a4fd7b5645f10f53
