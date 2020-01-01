from django.db import models


class Chat(models.Model):
    is_group_chat = models.BooleanField('Group chat')
    last_message = models.TextField('Last message', null=True, blank=True)
    name = models.CharField('Chat name', max_length=50)
    avatar = models.ImageField(upload_to='avatars/', null=True)
