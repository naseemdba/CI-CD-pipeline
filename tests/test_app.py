from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from CI/CD pipeline!"}

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_fail():
    client = app.test_client()
    response = client.get("/fail")
    assert response.status_code == 500
    assert response.get_json() == {"status": "error"}
