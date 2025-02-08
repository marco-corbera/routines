from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta
from routines.models import Exercise, Routine
from routines.serializers import ExerciseSerializer, RoutineSerializer


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """
        Returns the number of exercises done in a given period.
        Params: ?period=day/week/month/year
        """
        period = request.query_params.get('period', 'day')
        now = datetime.now()

        if period == 'day':
            start_date = now - timedelta(days=1)
        elif period == 'week':
            start_date = now - timedelta(weeks=1)
        elif period == 'month':
            start_date = now - timedelta(days=30)
        elif period == 'year':
            start_date = now - timedelta(days=365)
        else:
            return Response({"error": "Periodo inválido"}, status=400)

        exercises = Exercise.objects.filter(
            routine__user=request.user,
            routine__day__in=[now.strftime('%A'), start_date.strftime('%A')]
        ).count()

        return Response({"exercises_count": exercises})
    

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(routine__user=self.request.user)