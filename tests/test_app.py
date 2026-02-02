import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_list_stores(client):
    response = client.get("/stores")
    assert response.status_code == 200
    assert len(response.json["stores"]) == 5


def test_nearest_without_address(client):
    response = client.get("/nearest")
    assert response.status_code == 400


def test_nearest_with_address(client):
    response = client.get("/nearest?address=123+Main+St+New+York")
    assert response.status_code == 200
    assert "nearest" in response.json
