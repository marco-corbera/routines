import uuid
from django.db import models
from users.models import User


class Routine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="routines")
    name = models.CharField(max_length=255)
    day = models.CharField(max_length=20)
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.day} - {self.time})"


class Exercise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    routine = models.ForeignKey(
        Routine, on_delete=models.CASCADE, related_name="exercises"
    )
    name = models.CharField(max_length=255)
    sets = models.IntegerField(default=3)
    reps = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.name} ({self.sets} sets x {self.reps} reps)"
