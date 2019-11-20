from django.db import models


class Chat(models.Model):
    is_group_chat = models.BooleanField('Group chat')
    topic = models.TextField('Topic')
    last_message = models.TextField('Last message')
