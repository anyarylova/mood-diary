def test_invalid_token_rejected(client):
    headers = {"Authorization": "Bearer faketoken123"}
    res = client.get("/mood/", headers=headers)
    assert res.status_code == 401
    assert "Invalid token" in res.json()["detail"]
