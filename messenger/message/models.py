from django.db import models
from chats.models import Chat


class Message(models.Model):
    class Meta:
        ordering = (
            '-added_at',
        )

    chat = models.ForeignKey(Chat, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey('users.User', null=True,
                             on_delete=models.SET_NULL)

    content = models.TextField(max_length=1000)
    added_at = models.DateTimeField(auto_now=True)


class Attachment(models.Model):
    chat = models.ForeignKey(Chat, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    message = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL)

    TYPE = (
        (1, 'Image'),
        (2, 'Video'),
        (3, 'Voice message'),
    )
    attachment_type = models.PositiveSmallIntegerField(
        choices=TYPE,
        default=1,
    )
    url = models.URLField()
