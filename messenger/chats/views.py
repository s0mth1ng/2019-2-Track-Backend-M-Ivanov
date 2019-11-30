from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from chats.forms import ChatForm
from chats.models import Chat
from message.models import Message
from users.models import User, Member


def index(request):
    return render(request, 'chat.html')


def chat_detail(request, chat_id):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return HttpResponse('Chat does not exist')
    return JsonResponse({'id': chat.id,
                         'name': chat.name})


def chat_messages(request, chat_id):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    try:
        chat = Chat.objects.get(id=chat_id)
    except Chat.DoesNotExist:
        return HttpResponse('Chat does not exist')

    messages = Message.objects.filter(chat=chat)
    return JsonResponse({'data': list(messages.values())})


def chat_list(request, user_id):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponse('User does not exist')
    chat_ids = Member.objects.filter(
        user=user).values_list('chat_id', flat=True)
    chats = Chat.objects.filter(id__in=chat_ids)
    return JsonResponse({'data': list(chats.values())})


@csrf_exempt
def create_personal_chat(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    print(request.POST)
    form = ChatForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Chat created'})
    return JsonResponse({'errors': form.errors}, status=400)
