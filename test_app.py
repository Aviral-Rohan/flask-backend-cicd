"""Tests run by the Jenkins pipeline before every deployment."""
from app import app


def test_health_returns_ok():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_submit_accepts_valid_data():
    response = app.test_client().post("/submit", json={"name": "Rohan", "email": "rohan@example.com"})
    assert response.status_code == 201
    assert response.get_json()["data"]["name"] == "Rohan"


def test_submit_rejects_empty_fields():
    response = app.test_client().post("/submit", json={"name": "", "email": ""})
    assert response.status_code == 400
    assert "required" in response.get_json()["error"]
