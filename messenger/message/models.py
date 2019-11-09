from django.db import models
from chats.models import Chat


class Message(models.Model):
    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)

    content = models.TextField()
    added_at = models.DateTimeField()


class Attachment(models.Model):
    class Meta:
        verbose_name = 'attachment'
        verbose_name_plural = 'attachments'

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    type = models.CharField(max_length=16)
    url = models.URLField()
