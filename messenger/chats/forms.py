from django import forms

from chats.models import Chat
from users.models import User, Member


class ChatForm(forms.ModelForm):
    first_name = forms.CharField(max_length=25)
    second_name = forms.CharField(max_length=25)

    def clean_first_name(self):
        cleaned_name = self.cleaned_data['first_name']
        try:
            User.objects.get(name=cleaned_name)
        except User.DoesNotExist:
            self.add_error('first_name', 'User does not exist')
        return cleaned_name

    def clean_second_name(self):
        cleaned_name = self.cleaned_data['second_name']
        try:
            User.objects.get(name=cleaned_name)
        except User.DoesNotExist:
            self.add_error('second_name', 'User does not exist')
        return cleaned_name

    def clean(self):
        first = self.cleaned_data['first_tag']
        second = self.cleaned_data['second_tag']
        chat_name = '&'.join(sorted([first, second]))
        if Chat.objects.filter(name=chat_name).exists():
            self.add_error('chat', 'already exists')

    def save(self, **kwargs):
        first = self.cleaned_data['first_tag']
        second = self.cleaned_data['second_tag']

        chat_name = '&'.join(sorted([first, second]))
        chat = Chat.objects.create(
            name=chat_name,
            is_group_chat=False,
        )

        first_user = User.objects.get(name=first)
        Member.objects.create(
            user=first_user,
            chat=chat,
            new_messages=0,
        )
        second_user = User.objects.get(name=second)
        Member.objects.create(
            user=second_user,
            chat=chat,
            new_messages=0,
        )
