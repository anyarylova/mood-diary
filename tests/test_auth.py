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


def test_register_duplicate_user(client, test_user):
    # Register once
    client.post("/auth/register", json=test_user)
    # Try registering again
    res = client.post("/auth/register", json=test_user)
    assert res.status_code == 400
    assert "Username already taken" in res.json()["detail"]


def test_login_successful(client, test_user):
    client.post("/auth/register", json=test_user)
    res = client.post("/auth/login", data=test_user)
    assert res.status_code == 200
    assert "access_token" in res.json()
