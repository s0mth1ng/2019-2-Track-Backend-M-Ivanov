from django.core import serializers
from django.http import HttpResponseNotAllowed, JsonResponse

from message.forms import ReadMessageForm, SendMessageForm
from message.models import Message


def get_messages(request, chat_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    messages = Message.objects.filter(chat=chat_id)
    messages_serialized = serializers.serialize('json', messages)
    return JsonResponse(messages_serialized, safe=False)


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


def read_message(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    form = ReadMessageForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Message read'})
    else:
        return JsonResponse({'errors': form.errors}, status=400)
