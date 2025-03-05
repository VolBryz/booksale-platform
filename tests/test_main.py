# tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def clear_db():
    # Здесь вы можете делать очистку БД между тестами, если нужно
    pass

def test_create_seller(clear_db):
    data = {
        "first_name": "Ivan",
        "last_name": "Ivanov",
        "e_mail": "ivan@example.com",
        "password": "12345"
    }
    response = client.post("/api/v1/seller/", json=data)
    assert response.status_code == 201
    resp_json = response.json()
    assert resp_json["first_name"] == "Ivan"
    assert "password" not in resp_json

def test_get_sellers():
    response = client.get("/api/v1/seller/")
    assert response.status_code == 200
    sellers = response.json()
    for s in sellers:
        assert "password" not in s
