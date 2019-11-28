from django.core import serializers
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render

from chats.forms import ChatForm
from chats.models import Chat
from message.forms import SendMessageForm
from message.models import Message


def index(request):
    return render(request, 'chat.html')


def chat_detail(request, chat_id):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return HttpResponse('Chat does not exist')
    return JsonResponse(chat)


def chat_messages(request, chat_id):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return HttpResponse('Chat does not exist')

    messages = Message.objects.filter(chat=chat).values('id', 'user', 'content', 'added_at')
    return JsonResponse({
        'chat_id': chat_id,
        'messages': list(messages),
    })


def chat_list(request):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    chats = Chat.objects.all()
    chats_serialized = serializers.serialize('json', chats)
    return JsonResponse(chats_serialized, safe=False)


def create_personal_chat(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    form = ChatForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Chat created'})
    return JsonResponse({'errors': form.errors}, status=400)


def send_message(request):
    form = SendMessageForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Message sent'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)
