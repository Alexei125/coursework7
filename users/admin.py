from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("phone", "email")
    list_filter = ("email",)
    search_fields = ("email",)
