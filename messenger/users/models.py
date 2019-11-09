from django.db import models
from chats.models import Chat


class User(models.Model):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    name = models.CharField(max_length=32)
    nick = models.CharField(max_length=32)
    avatar = models.URLField()


class Member(models.Model):
    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    last_read_message = models.ForeignKey('message.Message', on_delete=models.CASCADE)
    new_messages = models.TextField()
