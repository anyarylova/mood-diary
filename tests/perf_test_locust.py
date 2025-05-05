import random
import string
import datetime
from locust import HttpUser, task, between
from requests.exceptions import HTTPError


def random_username():
    return "user_" + ''.join(
        random.choices(
            string.ascii_lowercase + string.digits, k=8
        )  # nosec B311
    )


class MoodDiaryUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(1, 2)

    def on_start(self):
        self.username = random_username()
        self.password = "testpass123"  # nosec B105
        self.token = None

        # Attempt to register
        try:
            res = self.client.post(
                "/auth/register",
                json={"username": self.username, "password": self.password},
                name="/auth/register"
            )
            if res.status_code == 400:
                # Already exists or failed? Try login
                res = self.client.post(
                    "/auth/login",
                    data={"username": self.username,
                          "password": self.password},
                    name="/auth/login"
                )

            self.token = res.json().get("access_token")

        except Exception as e:
            print("Auth failed:", e)
            self.token = None

    @task
    def log_mood(self):
        if not self.token:
            return
        headers = {"Authorization": f"Bearer {self.token}"}

        payload = {
            "mood": random.randint(0, 4),  # nosec B311
            "note": "Performance test mood entry",
            "date": datetime.date.today().isoformat()
        }

        try:
            res = self.client.post("/mood/", json=payload,
                                   headers=headers, name="/mood/")
            if res.status_code == 400:
                print("Duplicate mood or bad request.")
        except HTTPError as e:
            print("POST /mood/ error:", e)

    @task
    def get_stats(self):
        if not self.token:
            return
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("/stats/", headers=headers, name="/stats/")
