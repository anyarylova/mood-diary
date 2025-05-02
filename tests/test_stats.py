from datetime import date


def test_stats_endpoint(client):
    # Register and login
    client.post("/auth/register",
                json={"username": "statsuser", "password": "pass123"}
                )
    login = client.post("/auth/login",
                        data={"username": "statsuser", "password": "pass123"}
                        )
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Submit a few mood entries
    moods = [
        {"date": str(date(2024, 5, 1)), "mood": 2, "note": "Ok day"},
        {"date": str(date(2024, 5, 2)), "mood": 4, "note": "Great day"},
        {"date": str(date(2024, 5, 3)), "mood": 2, "note": "Same as usual"},
    ]
    for mood in moods:
        res = client.post("/mood/", json=mood, headers=headers)
        assert res.status_code == 200

    # Call the stats endpoint
    res = client.get("/stats/", headers=headers)
    assert res.status_code == 200
    data = res.json()

    # Assert expected keys
    assert "average_mood_score" in data
    assert "total_moods_logged" in data
    assert data["total_moods_logged"] == 3
    assert round(data["average_mood_score"], 2) == 2.67
    assert "most_common_mood" in data
