from django.contrib import admin

from .models import Chat


class ChatAdmin(admin.ModelAdmin):
    list_filter = ('last_message',)
    list_display = ('name', 'is_group_chat',)


admin.site.register(Chat, ChatAdmin)
