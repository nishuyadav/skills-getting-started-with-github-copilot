def test_signup_adds_participant(client, sample_activity):
    # Arrange
    email = "jane@mergington.edu"

    # Act
    response = client.post(f"/activities/{sample_activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {sample_activity}"}

    activities = client.get("/activities").json()
    assert email in activities[sample_activity]["participants"]


def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    email = "jane@mergington.edu"
    activity_name = "Nonexistent Activity"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
