from fastapi.testclient import TestClient
import pytest
from backend.app.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_root_welcome(client):
    """Test root endpoint response."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to Mood Diary API"}


def test_custom_openapi_schema(client):
    """Test custom OpenAPI schema is correctly generated."""
    # Force custom_openapi() to regenerate schema
    app.openapi_schema = None

    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()

    assert data["info"]["title"] == "Mood Diary API"
    assert data["info"]["version"] == "1.0.0"
    assert data["info"]
    assert data["info"]["description"] == (
        "Track your mood history with secure login."
    )
    assert "OAuth2PasswordBearer" in data["components"]["securitySchemes"]
    scheme = data["components"]["securitySchemes"]["OAuth2PasswordBearer"]
    assert scheme["type"] == "http"
    assert scheme["scheme"] == "bearer"
    assert scheme["bearerFormat"] == "JWT"

    for path in data["paths"].values():
        for method in path.values():
            assert {"OAuth2PasswordBearer": []} in method.get("security", [])
