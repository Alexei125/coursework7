from datetime import timedelta

from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habits(models.Model):
    creator_habit = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
        **NULLABLE,
    )
    place_habit = models.CharField(
        max_length=100, verbose_name="Место выполнения привычки", **NULLABLE
    )
    time_habit = models.TimeField(verbose_name="Время выполнения привычки", **NULLABLE)
    action_habit = models.CharField(max_length=100, verbose_name="Действие привычки")
    is_pleasant_habit = models.BooleanField(
        default=True, verbose_name="Признак приятной привычки"
    )
    connection_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="Связанная привычка", **NULLABLE
    )
    number_of_executions_habit = models.IntegerField(
        default=1, verbose_name="Количество выполнений привычки в неделю"
    )
    duration_habit = models.DurationField(
        default=timedelta(seconds=120),
        verbose_name="Продолжительность выполнения привычки",
    )
    is_published_habit = models.BooleanField(
        default=True, verbose_name="Признак публичности привычки"
    )
    reward_habit = models.CharField(
        max_length=100, verbose_name="Вознаграждение привычки", **NULLABLE
    )

    def __str__(self):
        return f"{self.action_habit} (создатель {self.creator_habit})"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
