from django.core import serializers
from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from message.forms import ReadMessageForm, SendMessageForm


@csrf_exempt
def send_message(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    form = SendMessageForm(request.POST)
    if form.is_valid():
        message = form.save()
        return JsonResponse({
            'msg': 'Message sent',
            'id': message.id,
        })
    return JsonResponse({'errors': form.errors}, status=400)


@csrf_exempt
def read_message(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    form = ReadMessageForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Message read'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)