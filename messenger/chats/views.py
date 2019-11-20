from django.http import JsonResponse, HttpResponseNotAllowed, Http404
from django.shortcuts import render


def index(request):
    return render(request, 'chat.html')


def get_chat(chat_id):
    return {'name': 'John Doe', 'chat_id': chat_id}


def chat_detail(request, chat_id):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    try:
        chat = get_chat(chat_id)
    except BaseException:
        raise Http404('No such user')
    return JsonResponse(chat)


def chat_list(request):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    return JsonResponse({1: {'name': 'user1'},
                         2: {'name': 'user2'}})
