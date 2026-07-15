import sys, os
import pytest

# Add repo root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask API is running" in response.data

def test_features(client):
    response = client.get("/features")
    assert response.status_code == 200
    data = response.get_json()
    assert "expected_features" in data
    assert len(data["expected_features"]) == 10

def test_predict_valid(client):
    payload = {"features": [3,1,22,1,0,7.25,0,1,2,0]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert "prediction" in data
    assert data["prediction"] in [0,1]

def test_predict_invalid(client):
    payload = {"features": [3,1,22]}  # too few features
    response = client.post("/predict", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
