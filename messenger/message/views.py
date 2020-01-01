from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from message.forms import ReadMessageForm, SendMessageForm, AttachFileForm


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


@csrf_exempt
def attach_file(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    form = AttachFileForm(request.POST, request.FILES)
    if form.is_valid():
        attachment = form.save()
        return JsonResponse({
            'attachment': {
                'id': attachment.id,
                'chat_id': attachment.chat.id,
                'user_id': attachment.user.id,
                'message': attachment.message.content,
                'type': attachment.attachment_type,
                'url': attachment.attachment_file.url,
            }
        })
    else:
        return JsonResponse({'errors': form.errors}, status=400)
