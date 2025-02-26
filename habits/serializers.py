from rest_framework import serializers

from habits.models import Habits
from habits.validators import (
    NotCombinationValidator,
    TimeDurationValidator,
    CombinationValidator,
    AbsenceValidator,
    FrequencyValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Habits."""

    class Meta:
        model = Habits
        fields = "__all__"

        validators = [
            NotCombinationValidator("connection_habit", "reward"),
            TimeDurationValidator("duration"),
            CombinationValidator("connection_habit", "habit_is_pleasant"),
            AbsenceValidator("habit_is_pleasant", "connection_habit", "reward"),
            FrequencyValidator("number_of_executions"),
        ]
