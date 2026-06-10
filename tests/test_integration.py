def test_signup_then_unregister_flow(client, sample_activity):
    # Arrange
    new_email = "integration.student@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{sample_activity}/signup", params={"email": new_email})
    activities_after_signup = client.get("/activities").json()
    unregister_response = client.delete(f"/activities/{sample_activity}/unregister", params={"email": new_email})
    activities_after_unregister = client.get("/activities").json()

    # Assert
    assert signup_response.status_code == 200
    assert new_email in activities_after_signup[sample_activity]["participants"]
    assert unregister_response.status_code == 200
    assert new_email not in activities_after_unregister[sample_activity]["participants"]
