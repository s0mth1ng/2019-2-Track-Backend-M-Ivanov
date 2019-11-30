from django.core import serializers
from django.http import JsonResponse, HttpResponseNotAllowed, Http404, HttpResponse
from django.shortcuts import render
from users.models import User, Member


def index(request):
    return render(request, 'profile.html')


def get_user(user_id):
    return User.objects.get(id=user_id)


def get_profile(request, user_id):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    try:
        user = get_user(user_id)
    except BaseException:
        raise Http404('No such user')
    return JsonResponse({'nick': user.nick,
                         'id': user.id})


def users_list(request):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    users = User.objects.all()
    return JsonResponse({'data': list(users.values_list())})


def find_profile(request):
    if request.method != 'GET':
        raise HttpResponseNotAllowed(['GET'])
    profiles = User.objects.filter(name__icontains=request.GET.get('name'))
    profiles = list(profiles.values('name'))
    return JsonResponse({'data': profiles})
