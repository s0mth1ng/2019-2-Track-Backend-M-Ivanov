from django.contrib import admin

from .models import Message, Attachment


class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('added_at',)
    list_display = ('chat', 'user', 'content',)


class AttachmentAdmin(admin.ModelAdmin):
    list_filter = ('message',)
    list_display = ('chat', 'user', 'message',)


admin.site.register(Message, MessageAdmin)
admin.site.register(Attachment, AttachmentAdmin)
