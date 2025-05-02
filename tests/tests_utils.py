def test_invalid_token(client):
    res = client.get("/mood/",
                     headers={"Authorization": "Bearer broken.token.here"})
    assert res.status_code == 401
