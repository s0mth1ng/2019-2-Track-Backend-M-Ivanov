from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render


def index(request):
    return render(request, 'profile.html')


def get_profile(request):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])

    profile_id = request.GET.get('profile_id')
    if profile_id:
        return JsonResponse({profile_id: {'name': 'smth'}})


def users_list(request):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    return JsonResponse({1: {'name': 'user1'},
                         2: {'name': 'user2'}})
