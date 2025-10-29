import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import Base, engine, SessionLocal

client = TestClient(app)

def setup_module(module):
    # create tables
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    # drop all tables (for cleanliness)
    Base.metadata.drop_all(bind=engine)

def test_register_and_login():
    payload = {"nombre":"Test User","email":"test@example.com","password":"pass123"}
    res = client.post("/auth/register", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["email"] == "test@example.com"

    # login
    res2 = client.post("/auth/login", json=payload)
    assert res2.status_code == 200
    token = res2.json().get("access_token")
    assert token is not None
