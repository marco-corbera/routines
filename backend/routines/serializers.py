from rest_framework import serializers
from routines.models import Exercise, Routine

class RoutineSerializer(serializers.ModelSerializer):
    exercises = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Routine
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'