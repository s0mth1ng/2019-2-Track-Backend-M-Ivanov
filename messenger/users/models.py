from django.db import models
from chats.models import Chat
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField("User's name", max_length=32)
    nick = models.CharField('Nickname', max_length=32)
    avatar = models.ImageField('Profile picture', upload_to='avatars/', blank=True)


class Member(models.Model):
    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'

    user = models.ForeignKey(
        User, verbose_name="User's name", null=True, on_delete=models.SET_NULL)
    chat = models.ForeignKey(Chat, verbose_name='Chat',
                             null=True, on_delete=models.SET_NULL)
    last_read_message = models.ForeignKey(
        'message.Message', null=True, blank=True, on_delete=models.SET_NULL)
    new_messages = models.TextField('New messages', null=True, blank=True)
