from django.contrib import admin
from routines.models import Routine, Exercise


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "day", "time", "user")
    list_filter = ("day", "user")
    search_fields = ("name", "user__username")


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sets", "reps", "routine")
    list_filter = ("routine",)
    search_fields = ("name", "routine__name")
