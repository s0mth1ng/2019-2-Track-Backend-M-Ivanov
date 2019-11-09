from users.views import index, get_profile, users_list
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('profile/', get_profile, name='get_profile'),
    path('list/', users_list, name='users_list'),
]
