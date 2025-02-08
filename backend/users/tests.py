import pytest
from routines.models import Routine

@pytest.mark.django_db
def test_create_routine(api_client, django_user_model):
    user = django_user_model.objects.create_user(username="testuser", password="password123")
    api_client.force_authenticate(user=user)
    payload = {"name": "Leg Day", "day": "Monday", "time": "18:00:00"}
    response = api_client.post("/api/routines/", payload, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "Leg Day"

@pytest.mark.django_db
def test_get_routines(api_client, django_user_model):
    user = django_user_model.objects.create_user(username="testuser", password="password123")
    api_client.force_authenticate(user=user)
    response = api_client.get("/api/routines/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_exercise(api_client, django_user_model):
    user = django_user_model.objects.create_user(username="testuser", password="password123")
    api_client.force_authenticate(user=user)
    routine = Routine.objects.create(user=user, name="Chest Day", day="Tuesday", time="19:00:00")
    payload = {"name": "Bench Press", "sets": 4, "reps": 12, "routine": routine.id}
    response = api_client.post("/api/exercises/", payload, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "Bench Press"