def test_signup_then_unregister_flow(client):
    # Arrange
    activity_name = "Programming Class"
    email = "flow.student@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    after_signup = client.get("/activities").json()[activity_name]["participants"]

    unregister_response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )
    after_unregister = client.get("/activities").json()[activity_name]["participants"]

    # Assert
    assert signup_response.status_code == 200
    assert email in after_signup
    assert unregister_response.status_code == 200
    assert email not in after_unregister
