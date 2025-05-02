def test_register_and_login(client):
    # Step 1: Register a new user
    response = client.post("/auth/register", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "msg" in response.json()
    assert "registered successfully" in response.json()["msg"]

    # Step 2: Login with that user
    response = client.post("/auth/login", data={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
