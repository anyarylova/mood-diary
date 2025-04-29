import requests
from datetime import datetime, timedelta
import random

API_URL = "http://localhost:8000"

# Credentials
username = "demo_user"
password = "demo_pass"

# 1. Register user
reg_res = requests.post(f"{API_URL}/auth/register", json={"username": username, "password": password})

# 2. Login user
login_res = requests.post(f"{API_URL}/auth/login", data={"username": username, "password": password})

if login_res.status_code != 200:
    print("Login failed:", login_res.json())
    exit()

token = login_res.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# 3. Group notes by mood type
notes_by_mood = {
    0: [  # Sad
        "Lost my dog today 💔",
        "Failed my math exam... 😞",
        "Sick day, stayed in bed 🤒",
        "Missed my best friend today 😔",
        "Bad weather made me feel gloomy 🌧️",
    ],
    1: [  # Low
        "Feeling very stressed about finals 😰",
        "Long meeting at work... very tired 💤",
        "Feeling overwhelmed but managing 🙃",
    ],
    2: [  # Neutral
        "Had a peaceful day reading a book 📚",
        "Watched a great movie 🍿",
        "Learned something new in coding! 👨‍💻",
        "Started a new hobby 🎨",
    ],
    3: [  # Happy
        "Family trip was so fun! 🏖️",
        "Went to the gym and felt great 💪",
        "Randomly happy today, no reason! 😄",
        "Had an amazing day with friends! 🎉",
    ],
    4: [  # Excited
        "Got an A+ in my final exam! 🏆",
        "Got a promotion at work! 🚀",
        "Celebrated my birthday! 🎂",
        "Feeling grateful for everything 🙏",
    ]
}

# 4. Insert moods for the last 30 days
today = datetime.today()

for i in range(30):
    day = today - timedelta(days=i)
    mood = random.randint(0, 4)
    note = random.choice(notes_by_mood[mood])  # pick a note matching the mood

    mood_data = {
        "date": day.date().isoformat(),
        "mood": mood,
        "note": note
    }
    res = requests.post(f"{API_URL}/mood/", json=mood_data, headers=headers)
    if res.status_code == 200:
        print(f"Added mood for {day.date()}: {note}")
    else:
        print(f"Failed for {day.date()}: {res.json()}")
