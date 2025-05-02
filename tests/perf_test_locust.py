from locust import HttpUser, task, between

class MoodDiaryUser(HttpUser):
    wait_time = between(1, 2)  # Simulate realistic wait between requests

    def on_start(self):
        # Register or login
        self.username = "locustuser"
        self.password = "locustpass"

        # Try to register (ignore if already exists)
        self.client.post("/auth/register", json={"username": self.username, "password": self.password})

        # Login to get token
        res = self.client.post("/auth/login", data={"username": self.username, "password": self.password})
        self.token = res.json().get("access_token", None)
        self.headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}

    @task
    def log_mood(self):
        self.client.post("/mood/", json={
            "mood": 2,
            "note": "Performance test entry",
            "date": "2024-05-01"
        }, headers=self.headers)

    @task
    def view_stats(self):
        self.client.get("/stats/", headers=self.headers)
