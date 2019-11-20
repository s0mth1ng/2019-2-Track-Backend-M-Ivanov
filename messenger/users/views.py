from django.http import JsonResponse, HttpResponseNotAllowed, Http404
from django.shortcuts import render


def index(request):
    return render(request, 'profile.html')


def get_user(user_id):
    return {'user_id': user_id, 'name': 'John Doe'}


def get_profile(request, user_id):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    try:
        user = get_user(user_id)
    except BaseException:
        raise Http404('No such user')
    return JsonResponse(user)


def users_list(request):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    return JsonResponse({1: {'name': 'user1'},
                         2: {'name': 'user2'}})
