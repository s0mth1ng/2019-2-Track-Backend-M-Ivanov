from chats.views import index, chat_detail, chat_list, create_personal_chat, chat_messages
from django.urls import path

from message.views import send_message, read_message, attach_file

urlpatterns = [
    path('index/', index, name='index'),
    path('detail/<int:chat_id>', chat_detail, name='chat_detail'),
    path('list/<int:user_id>', chat_list, name='chat_list'),
    path('create_chat/', create_personal_chat, name='create_personal_chat'),
    path('messages/<int:chat_id>', chat_messages, name='chat_messages'),
    path('send/', send_message, name='send_message'),
    path('read/', read_message, name='read_message'),
    path('attach/', attach_file, name='attach_file'),
]
