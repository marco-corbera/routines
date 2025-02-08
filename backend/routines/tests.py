import pytest


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_user(api_client):
    payload = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    }
    response = api_client.post("/api/signup/", payload, format="json")
    assert response.status_code == 201
    assert response.data["message"] == "User created successfully"

@pytest.mark.django_db
def test_user_login(api_client, django_user_model):
    user = django_user_model.objects.create_user(username="testuser", password="password123")
    payload = {"username": "testuser", "password": "password123"}
    response = api_client.post("/api/token/", payload, format="json")
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data