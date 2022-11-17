from fastapi.testclient import TestClient

from dice_fastapi.app import app, roll_dice

client = TestClient(app)


def test_dice_roll():
    results = [roll_dice() for _ in range(100)]
    assert min(results) == 1
    assert max(results) == 6


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "result" in response.json()
    assert 1 <= response.json()["result"] <= 6
