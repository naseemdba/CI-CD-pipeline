import json
from app import app

def test_health_ok():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_fail_route():
    client = app.test_client()
    response = client.get("/fail")
    assert response.status_code == 500
