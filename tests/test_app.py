from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def reset_activities():
    activities["Chess Club"]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]


def test_unregister_participant_removes_email():
    reset_activities()

    response = client.delete("/activities/Chess Club/participants?email=michael@mergington.edu")

    assert response.status_code == 200
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"


def test_unregister_missing_participant_returns_404():
    reset_activities()

    response = client.delete("/activities/Chess Club/participants?email=student@mergington.edu")

    assert response.status_code == 404
