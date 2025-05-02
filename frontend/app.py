import streamlit as st
import requests
from datetime import date
from enum import IntEnum
import pandas as pd
import altair as alt
import html

API_URL = "http://localhost:8000"


class MoodEnum(IntEnum):
    sad = 0
    low = 1
    neutral = 2
    happy = 3
    excited = 4


# Session state initialization
if "token" not in st.session_state:
    st.session_state.token = None
if "user" not in st.session_state:
    st.session_state.user = None


# Headers with token
def get_headers():
    if st.session_state.token:
        return {"Authorization": f"Bearer {st.session_state.token}"}
    return {}


# Authentication form
def auth_form():
    st.subheader("Login or Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(
            f"{API_URL}/auth/login",
            data={"username": username, "password": password}
        )
        if res.status_code == 200:
            st.session_state.token = res.json()["access_token"]
            st.session_state.user = username
            st.success("Logged in!")
            st.rerun()
        else:
            error_detail = res.json().get("detail", "Login failed.")
            st.error(error_detail)

    if st.button("Register"):
        res = requests.post(
            f"{API_URL}/auth/register",
            json={"username": username, "password": password}
        )
        if res.status_code == 200:
            st.success("Registered! Now log in.")
        else:
            error_detail = res.json().get("detail", "Registration failed.")
            st.error(error_detail)


# Mood entry form
def mood_entry_form():
    st.subheader("Log a Mood")
    mood_options = {
        "1 - 😔 Sad": 0,
        "2 - 🙁 Low": 1,
        "3 - 🙂 Neutral": 2,
        "4 - 😊 Happy": 3,
        "5 - 😄 Excited": 4
    }
    mood_str = st.selectbox(
        "How do you feel today?", list(mood_options.keys()))
    description = st.text_area("Describe your mood")
    entry_date = st.date_input("Date", value=date.today())

    if st.button("Submit Mood"):
        mood_int = mood_options[mood_str]
        res = requests.post(
            f"{API_URL}/mood/",
            json={
                "mood": mood_int,
                "note": description,
                "date": entry_date.isoformat()
            },
            headers=get_headers()
        )
        if res.status_code == 200:
            st.success("Mood logged successfully!")
        else:
            st.error(res.json().get("detail", "Failed to log mood."))


# View mood history
def view_moods():
    st.subheader("📖 Mood History")
    res = requests.get(f"{API_URL}/mood/", headers=get_headers())

    if res.status_code == 200:
        moods = res.json()
        if not moods:
            st.info("You haven't logged any moods yet.")
            return

        moods = sorted(moods, key=lambda x: x["date"], reverse=True)

        mood_map = {
            0: "😔 Sad",
            1: "🙁 Low",
            2: "🙂 Neutral",
            3: "😊 Happy",
            4: "😄 Excited"
        }

        for m in moods:
            mood_label = mood_map.get(m["mood"], "Unknown Mood")
            date_str = m["date"]
            note = m.get("note", "No description.")

            with st.container():
                st.markdown(f"### {mood_label} ({date_str})")
                st.write(f"**Note:** {html.escape(note)}")
                st.markdown("---")
    else:
        st.error(res.json().get("detail", "Failed to load mood history."))


def view_stats():
    st.subheader("📊 Mood Statistics")
    res = requests.get(f"{API_URL}/stats/", headers=get_headers())
    if res.status_code == 200:
        stats = res.json()

        if "message" in stats:
            st.info(stats["message"])
            return

        total_logged = stats.get("total_moods_logged", 0)
        average_mood = stats.get("average_mood_score", 0)

        st.metric("Total Moods Logged", total_logged)
        st.metric("Average Mood Score", average_mood)

        mood_message = ""
        if average_mood <= 1.5:
            mood_message = (
                "😔 It's been tough lately. it's okay to have bad days!"
            )
        elif 1.5 < average_mood <= 2.5:
            mood_message = "🙁 Hang in there! Brighter days are coming."
        elif 2.5 < average_mood <= 3.5:
            mood_message = "🙂 You're keeping it balanced. Good job!"
        elif 3.5 < average_mood <= 4.5:
            mood_message = "😊 Great mood vibes! Keep it up!"
        else:
            mood_message = "😄 Amazing positivity! You're shining bright!"

        st.info(mood_message)

        st.markdown("### 🏆 Best Day")
        st.write(f"**Date:** {stats['best_day']['date']}")
        st.write(f"**Mood:** {stats['best_day']['mood']}")
        st.write(f"**Note:** {html.escape(stats['best_day']['note'])}")

        st.markdown("### 💔 Worst Day")
        st.write(f"**Date:** {stats['worst_day']['date']}")
        st.write(f"**Mood:** {stats['worst_day']['mood']}")
        st.write(f"**Note:** {html.escape(stats['worst_day']['note'])}")

        st.markdown("### 😀 Most Common Mood")
        st.success(stats.get("most_common_mood", "N/A"))
    else:
        st.error(res.json().get("detail", "Failed to fetch stats."))


def view_graph():
    st.subheader("Mood Graph for the Last Month")
    res = requests.get(f"{API_URL}/mood/", headers=get_headers())

    if res.status_code == 200:
        moods = res.json()
        if not moods:
            st.info("No mood entries to show.")
            return

        df = pd.DataFrame(moods)
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")

        last_month = pd.Timestamp.today() - pd.Timedelta(days=30)
        df_last_month = df[df["date"] >= last_month]

        mood_map = {
            0: "😔 Sad",
            1: "🙁 Low",
            2: "🙂 Neutral",
            3: "😊 Happy",
            4: "😄 Excited"
        }
        score_map = {k: k + 1 for k in mood_map}

        df_last_month["mood_score"] = df_last_month["mood"].map(score_map)
        df_last_month["mood_label"] = df_last_month["mood"].map(mood_map)

        if not df_last_month.empty:
            chart = alt.Chart(df_last_month).mark_line(point=True).encode(
                x=alt.X("date:T", title="Date"),
                y=alt.Y("mood_score:Q", title="Mood Score"),
                tooltip=[
                    alt.Tooltip("date:T", title="Date"),
                    alt.Tooltip("mood_label:N", title="Mood"),
                    alt.Tooltip("note:N", title="Note")
                ]
            ).properties(
                width=700,
                height=400,
                title="Mood Changes Over Last 30 Days"
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("No moods recorded in the past month.")
    else:
        st.error(res.json().get("detail", "Failed to load moods."))


def view_calendar():
    st.subheader("📅 Mood Calendar")
    res = requests.get(f"{API_URL}/mood/", headers=get_headers())

    if res.status_code != 200:
        st.error(res.json().get("detail", "Failed to load moods."))
        return

    moods = res.json()
    if not moods:
        st.info("No mood entries to show.")
        return

    df = pd.DataFrame(moods)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.strftime("%B")

    available_months = sorted(
        df[["month", "year", "month_name"]].drop_duplicates().to_records(
            index=False
        ),
        key=lambda x: (x[1], x[0]),
        reverse=True
    )

    selected = st.selectbox(
        "Select Month to View:",
        available_months,
        format_func=lambda x: f"{x[2]} {x[1]}"
    )
    selected_month, selected_year, _ = selected

    df = df[(df["month"] == selected_month) & (df["year"] == selected_year)]
    if df.empty:
        st.info("No moods recorded for the selected month.")
        return

    df["day"] = df["date"].dt.day
    df["weekday"] = df["date"].dt.weekday
    df["week"] = df["date"].dt.isocalendar().week

    mood_map = {
        0: "😔", 1: "🙁", 2: "🙂", 3: "😊", 4: "😄"
    }
    mood_label_map = {
        0: "Sad", 1: "Low", 2: "Neutral", 3: "Happy", 4: "Excited"
    }
    df["emoji"] = df["mood"].map(mood_map)
    df["mood_label"] = df["mood"].map(mood_label_map)

    chart = alt.Chart(df).mark_text(
        align="center",
        baseline="middle",
        size=30
    ).encode(
        x=alt.X(
            "weekday:O",
            title="Day of Week",
            axis=alt.Axis(
                labels=True,
                labelExpr='["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]'
                "[datum.value]"
            )
        ),
        y=alt.Y("week:O", title="Week"),
        text="emoji:N",
        tooltip=[
            alt.Tooltip("date:T", title="Date"),
            alt.Tooltip("mood_label:N", title="Mood"),
            alt.Tooltip("note:N", title="Note")
        ]
    ).properties(
        width=600,
        height=300,
        title=f"Mood Calendar - {selected[2]} {selected[1]}"
    )

    st.altair_chart(chart, use_container_width=True)


def get_today_quote():
    try:
        res = requests.get("https://zenquotes.io/api/today", timeout=5)
        if res.status_code == 200:
            data = res.json()[0]
            return f'"{data["q"]}" — {data["a"]}'
    except requests.RequestException:
        return None


# Main UI
st.title("📝 Mood Diary")
st.title("Quote of the day")
quote = get_today_quote()
if quote:
    st.info(f"💬 {quote}")


if not st.session_state.user or not st.session_state.token:
    auth_form()
else:
    st.sidebar.write(f"👋 Hello, {st.session_state.user}")
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.session_state.token = None
        st.rerun()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Log Mood", "View History", "View Stats", "Mood Graph", "Calendar"]
    )

    if page == "Log Mood":
        mood_entry_form()
    elif page == "View History":
        view_moods()
    elif page == "View Stats":
        view_stats()
    elif page == "Mood Graph":
        view_graph()
    elif page == "Calendar":
        view_calendar()
