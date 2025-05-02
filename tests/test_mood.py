from datetime import date

def test_submit_and_get_mood(client):
    # Register and login to get access token
    register = client.post("/auth/register", json={"username": "moodtester", "password": "pass123"})
    assert register.status_code == 200

    login = client.post("/auth/login", data={"username": "moodtester", "password": "pass123"})
    assert login.status_code == 200
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Submit a mood
    payload = {
        "date": str(date.today()),
        "mood": 4,
        "note": "Feeling great today!"
    }
    res = client.post("/mood/", json=payload, headers=headers)
    assert res.status_code == 200
    assert res.json()["mood"] == 4
    assert res.json()["note"] == "Feeling great today!"

    # Get mood history
    res = client.get("/mood/", headers=headers)
    assert res.status_code == 200
    moods = res.json()
    assert isinstance(moods, list)
    assert any(m["note"] == "Feeling great today!" for m in moods)


def test_duplicate_mood_rejected(client):
    client.post("/auth/register", json={"username": "dupuser", "password": "pass123"})
    login = client.post("/auth/login", data={"username": "dupuser", "password": "pass123"})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    mood_payload = {
        "date": str(date.today()),
        "mood": 3,
        "note": "First entry"
    }

    # First submission should pass
    res1 = client.post("/mood/", json=mood_payload, headers=headers)
    assert res1.status_code == 200

    # Second submission for same date should fail
    res2 = client.post("/mood/", json=mood_payload, headers=headers)
    assert res2.status_code == 400
    assert "already exists" in res2.json()["detail"]
