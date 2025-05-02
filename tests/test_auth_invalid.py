def test_invalid_token_rejected(client):
    headers = {"Authorization": "Bearer faketoken123"}
    res = client.get("/mood/", headers=headers)
    assert res.status_code == 401
    assert "Invalid token" in res.json()["detail"]


def test_login_wrong_password(client, test_user):
    client.post("/auth/register", json=test_user)
    res = client.post("/auth/login", data={"username": test_user["username"], "password": "wrong"})
    assert res.status_code == 401


def test_login_unknown_user(client):
    res = client.post("/auth/login", data={"username": "ghost", "password": "ghost123"})
    assert res.status_code == 401
