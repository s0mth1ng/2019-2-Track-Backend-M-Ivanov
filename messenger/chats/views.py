from django.http import JsonResponse, HttpResponseNotAllowed, Http404
from django.shortcuts import render


def index(request):
    return render(request, 'chat.html')


def chat_detail(request):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])

    chat_id = request.GET.get('chat_id')
    if chat_id:
        return JsonResponse({chat_id: {'name': 'smth'}})

    raise Http404('No such user')


def chat_list(request):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    return JsonResponse({1: {'name': 'user1'},
                         2: {'name': 'user2'}})
