from django import forms

from chats.models import Chat
from users.models import User, Member


class ChatForm(forms.Form):
    first_nick = forms.CharField(max_length=32)
    second_nick = forms.CharField(max_length=32)

    def clean_first_nick(self):
        cleaned_nick = self.cleaned_data['first_nick']
        try:
            User.objects.get(nick=cleaned_nick)
        except User.DoesNotExist:
            self.add_error('first_nick', 'User does not exist')
        return cleaned_nick

    def clean_second_nick(self):
        cleaned_nick = self.cleaned_data['second_nick']
        try:
            User.objects.get(nick=cleaned_nick)
        except User.DoesNotExist:
            self.add_error('second_nick', 'User does not exist')
        return cleaned_nick

    def clean(self):
        if len(self.errors) == 0:
            first = self.cleaned_data['first_nick']
            second = self.cleaned_data['second_nick']
            chat_name = '&'.join(sorted([first, second]))
            if Chat.objects.filter(name=chat_name).exists():
                self.add_error(None, 'Chat already exists')

    def save(self, **kwargs):
        first = self.cleaned_data['first_nick']
        second = self.cleaned_data['second_nick']

        chat_name = '&'.join(sorted([first, second]))
        chat = Chat.objects.create(
            name=chat_name,
            is_group_chat=False,
        )

        first_user = User.objects.get(nick=first)
        Member.objects.create(
            user=first_user,
            chat=chat,
        )
        second_user = User.objects.get(nick=second)
        Member.objects.create(
            user=second_user,
            chat=chat,
        )
        return chat