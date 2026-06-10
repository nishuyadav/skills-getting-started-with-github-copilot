def test_unregister_removes_participant(client, sample_activity):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.delete(f"/activities/{sample_activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {sample_activity}"}

    activities = client.get("/activities").json()
    assert email not in activities[sample_activity]["participants"]


def test_unregister_nonexistent_activity_returns_404(client):
    # Arrange
    email = "jane@mergington.edu"
    activity_name = "Nonexistent Activity"

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_missing_participant_returns_400(client, sample_activity, sample_email):
    # Arrange
    email = sample_email

    # Act
    response = client.delete(f"/activities/{sample_activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not registered for this activity"
