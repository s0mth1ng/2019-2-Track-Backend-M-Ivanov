from django import forms

from chats.models import Chat
from message.models import Message
from users.models import Member, User


class SendMessageForm(forms.Form):
    chat_id = forms.IntegerField()
    user_id = forms.IntegerField()
    content = forms.CharField(max_length=1000)

    def clean_chat_id(self):
        chat_id = self.cleaned_data['chat_id']
        if not Chat.objects.filter(id=chat_id).exists():
            self.add_error('chat_id', 'Chat does not exist')
        return chat_id

    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        if not User.objects.filter(id=user_id).exists():
            self.add_error('user_id', 'User does not exist')
        return user_id

    def save(self):
        chat = Chat.objects.get(id=self.cleaned_data.get('chat_id'))
        user = User.objects.get(id=self.cleaned_data.get('user_id'))
        content = self.cleaned_data['content']
        return Message.objects.create(user=user, chat=chat, content=content)


class ReadMessageForm(forms.Form):
    message_id = forms.IntegerField()
    chat_id = forms.IntegerField()
    user_id = forms.IntegerField()

    def clean_message_id(self):
        message_id = self.cleaned_data['message_id']
        if not Message.objects.filter(id=message_id).exists():
            self.add_error('message_id', 'Message does not exist')
        return message_id

    def clean_chat_id(self):
        chat_id = self.cleaned_data['chat_id']
        if not Chat.objects.filter(id=chat_id).exists():
            self.add_error('chat_id', 'Chat does not exist')
        return chat_id

    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        if not User.objects.filter(id=user_id).exists():
            self.add_error('user_id', 'User does not exist')
        return user_id

    def clean(self):
        chat = Chat.objects.get(id=self.cleaned_data.get('chat_id'))
        user = User.objects.get(id=self.cleaned_data.get('user_id'))
        message = Message.objects.get(id=self.cleaned_data['message_id'])
        if not Member.objects.filter(chat=chat, user=user).exists():
            self.add_error('user_id', 'User does not exist')

    def save(self):
        chat = Chat.objects.get(id=self.cleaned_data['chat_id'])
        user = User.objects.get(id=self.cleaned_data['user_id'])
        message = Message.objects.get(id=self.cleaned_data['message_id'])
        member = Member.objects.get(chat=chat, user=user)
        if member.last_read_message.added_at < message.added_at:
            member.last_read_message = message
            member.save()
