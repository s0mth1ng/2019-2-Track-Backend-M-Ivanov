from django.db import models
from chats.models import Chat
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField("User's name", max_length=32)
    nick = models.CharField('Nickname', max_length=32)
    avatar = models.ImageField('Profile picture')


class Member(models.Model):
    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'

    user = models.ForeignKey(User, verbose_name="User's name", on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, verbose_name='Chat', on_delete=models.CASCADE)
    last_read_message = models.ForeignKey('message.Message', verbose_name='Last read message', on_delete=models.CASCADE)
    new_messages = models.TextField('New messages')
