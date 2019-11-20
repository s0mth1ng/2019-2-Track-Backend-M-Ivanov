from chats.views import index, chat_detail, chat_list
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('detail/<int:chat_id>', chat_detail, name='chat_detail'),
    path('list/', chat_list, name='chat_list'),
]
