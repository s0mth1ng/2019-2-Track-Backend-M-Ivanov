from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_filter = ('nick',)
    list_display = ('name', 'nick',)


admin.site.register(User, UserAdmin)
