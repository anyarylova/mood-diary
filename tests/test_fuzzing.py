from fastapi.testclient import TestClient
from hypothesis import given, strategies as st, settings, HealthCheck
from datetime import date, timedelta

# Strategies for fuzzing
safe_characters = st.characters(
    whitelist_categories=('L', 'N', 'P', 'S', 'Z')
)
general_text = st.text(
    alphabet=safe_characters,
    min_size=0,
    max_size=255
)
password_strategy = st.text(
    alphabet=safe_characters,
    min_size=6,
    max_size=100
)
note_strategy = st.text(
    alphabet=safe_characters,
    min_size=0,
    max_size=5000
)
valid_username_chars = st.characters(
    whitelist_categories=('L', 'N'),
    min_codepoint=65,
    max_codepoint=122
)
valid_username = st.text(
    alphabet=valid_username_chars,
    min_size=3,
    max_size=50
)
min_date = date(1970, 1, 1)
max_date = date.today() + timedelta(days=365)
date_strategy = st.dates(min_value=min_date, max_value=max_date)
mood_int_strategy = st.integers(min_value=-10, max_value=10)
valid_mood_int_strategy = st.integers(min_value=0, max_value=4)
invalid_mood_int_strategy = st.integers().filter(lambda x: not (0 <= x <= 4))


# Fuzzing Registration
@settings(
    max_examples=50,
    deadline=None,
    suppress_health_check=[HealthCheck.function_scoped_fixture]
)
@given(username=general_text, password=password_strategy)
def test_fuzz_register(client: TestClient, username, password):
    response = client.post("/auth/register", json={
        "username": username,
        "password": password
    })
    # Expect success (200), duplicate error (400), or validation error (422)
    # Should not cause a server error (500)
    assert response.status_code in [200, 400, 422]


# Fuzzing Login
@settings(
    max_examples=50,
    deadline=None,
    suppress_health_check=[HealthCheck.function_scoped_fixture]
)
@given(username=general_text, password=password_strategy)
def test_fuzz_login(client: TestClient, username, password):
    response = client.post("/auth/login", data={
        "username": username,
        "password": password
    })
    # Expect unauthorized (401) or validation error (422)
    # Should not cause a server error (500)
    assert response.status_code in [401, 422]


# Fuzzing Mood Creation
@settings(
    max_examples=50,
    deadline=None,
    suppress_health_check=[HealthCheck.function_scoped_fixture]
)
@given(
    mood_date=date_strategy,
    mood_value=mood_int_strategy,
    note=note_strategy
)
def test_fuzz_create_mood(authorized_headers: dict,
                          client: TestClient,
                          mood_date,
                          mood_value,
                          note):
    payload = {
        "date": str(mood_date),
        "mood": mood_value,
        "note": note
    }
    response = client.post("/mood/", json=payload, headers=authorized_headers)

    # Expect success (200), duplicate error (400),
    # unauthorized (401), or validation error (422)
    # Should not cause a server error (500)

    assert response.status_code in [200, 400, 422, 401]


# Fuzzing Mood Creation with Valid and Invalid Mood Values
@settings(
    max_examples=50,
    deadline=None,
    suppress_health_check=[HealthCheck.function_scoped_fixture]
)
@given(
    mood_date=date_strategy,
    mood_value=valid_mood_int_strategy,
    note=note_strategy
)
def test_fuzz_create_mood_valid(authorized_headers: dict,
                                client: TestClient,
                                mood_date,
                                mood_value,
                                note):
    payload = {"date": str(mood_date), "mood": mood_value, "note": note}
    response = client.post("/mood/", json=payload, headers=authorized_headers)
    # Expect success (200) or duplicate error (400)
    assert response.status_code in [200, 400]


@settings(
    max_examples=50,
    deadline=None,
    suppress_health_check=[HealthCheck.function_scoped_fixture]
)
@given(
    mood_date=date_strategy,
    mood_value=invalid_mood_int_strategy,
    note=note_strategy
)
def test_fuzz_create_mood_invalid(authorized_headers: dict,
                                  client: TestClient,
                                  mood_date,
                                  mood_value,
                                  note):
    payload = {"date": str(mood_date), "mood": mood_value, "note": note}
    response = client.post("/mood/", json=payload, headers=authorized_headers)
    # Expect validation error (422) or duplicate error (400)
    assert response.status_code in [400, 422]
