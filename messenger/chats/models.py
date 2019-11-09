from django.db import models


class Chat(models.Model):
    class Meta:
        verbose_name = 'chat'
        verbose_name_plural = 'chats'

    is_group_chat = models.BooleanField()
    topic = models.TextField()
    last_message = models.TextField()
