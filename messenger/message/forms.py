from django import forms
from django.core.files.images import ImageFile

from chats.models import Chat
from message.models import Message, Attachment
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
        if member.last_read_message is not None and member.last_read_message.added_at < message.added_at:
            member.last_read_message = message
            member.save()


class AttachFileForm(forms.Form):
    chat_id = forms.IntegerField()
    user_id = forms.IntegerField()
    file_type = forms.IntegerField()
    file_path = forms.CharField(max_length=1000)

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

    def clean_file_type(self):
        file_type = self.cleaned_data['file_type']
        available_types = [t[0] for t in Attachment.TYPE]
        if file_type not in available_types:
            self.add_error(None, 'Type does not exist')
        return file_type

    def clean_file_path(self):
        file_path = self.cleaned_data.get('file_path')
        try:
            ImageFile(open(file_path, 'rb'))
        except FileNotFoundError:
            self.add_error('file_path', 'File does not exist')
        return file_path

    def save(self):
        chat = Chat.objects.get(id=self.cleaned_data.get('chat_id'))
        user = User.objects.get(id=self.cleaned_data.get('user_id'))
        file_type = self.cleaned_data.get('file_type')
        file_path = self.cleaned_data.get('file_path')
        file = ImageFile(open(file_path, 'rb'))
        message = Message.objects.create(chat=chat, user=user)
        attachment = Attachment.objects.create(chat=chat,
                                               user=user,
                                               message=message,
                                               attachment_type=file_type,
                                               attachment_file=file, )
        return attachment
