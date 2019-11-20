from django.db import models
from chats.models import Chat


class Message(models.Model):
    class Meta:
        ordering = ('-added_at',)

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)

    content = models.TextField()
    added_at = models.DateTimeField()


class Attachment(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    TYPE = (
        (1, 'Image'),
        (2, 'Video'),
    )
    attachment_type = models.PositiveSmallIntegerField(
        choices=TYPE,
        default=1,
    )
    url = models.URLField()
