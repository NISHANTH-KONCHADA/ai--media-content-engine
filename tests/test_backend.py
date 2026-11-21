from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "IncuBrix Engine" in response.text

def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "HEALTHY"
    assert "ram_total_gb" in data

def test_brand():
    response = client.get("/api/brand")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "IncuBrix"
    assert "#4F46E5" in data["primary_color"]

def test_research():
    r_obs = client.get("/api/research/observations")
    assert r_obs.status_code == 200
    assert len(r_obs.json()) == 5

    r_opp = client.get("/api/research/opportunities")
    assert r_opp.status_code == 200
    assert len(r_opp.json()) == 3

    r_comp = client.get("/api/research/competitors")
    assert r_comp.status_code == 200
    assert len(r_comp.json()) == 6

def test_audience_stats():
    resp = client.get("/api/audience/stats")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "COMPLETED"
    assert data["sample_size"] == 22
    assert data["variant_a"]["votes"] == 16
    assert data["beats_benchmark"] is True
