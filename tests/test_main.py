from fastapi.testclient import TestClient


# Test the root endpoint '/'
def test_read_root(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to Mood Diary API"}


# Test if the OpenAPI schema endpoint '/openapi.json' works correctly
def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert "openapi" in schema
    assert "info" in schema
    assert "paths" in schema
    assert "components" in schema
    assert schema["info"]["title"] == "Mood Diary API"
    assert "securitySchemes" in schema["components"]
    assert "OAuth2PasswordBearer" in schema["components"]["securitySchemes"]
    assert "/mood/" in schema["paths"]
    assert "post" in schema["paths"]["/mood/"]
    assert isinstance(schema["paths"]["/mood/"]["post"].get("security"), list)
    assert len(schema["paths"]["/mood/"]["post"]["security"]) > 0
    passwordBearer = schema["paths"]["/mood/"]["post"]["security"][0]
    assert "OAuth2PasswordBearer" in passwordBearer
