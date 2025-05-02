import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.database import Base, get_db
from backend.app.main import app

# Setup a separate test DB (file-based for simplicity)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


# Fixture for DB
@pytest.fixture(scope="function")
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Fixture for test client
@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


# Fixture: test user credentials
@pytest.fixture
def test_user():
    return {"username": "testuser", "password": "testpass123"}


# Fixture: register test user
@pytest.fixture
def registered_user(client, test_user):
    client.post("/auth/register", json=test_user)
    return test_user


# Fixture: authorized headers with token
@pytest.fixture
def authorized_headers(client, registered_user):
    response = client.post("/auth/login", data=registered_user)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
