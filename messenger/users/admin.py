from django.contrib import admin
from users.models import User, Member


class UserAdmin(admin.ModelAdmin):
    list_filter = ('nick',)
    list_display = ('id', 'name', 'nick',)


class MemberAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = ('id', 'user', 'chat',)


admin.site.register(User, UserAdmin)
admin.site.register(Member, MemberAdmin)
