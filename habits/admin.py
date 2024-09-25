from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "action_habit",
        "creator_habit",
        "is_published_habit",
    )
    list_filter = ("creator_habit",)
    search_fields = ("action_habit",)
