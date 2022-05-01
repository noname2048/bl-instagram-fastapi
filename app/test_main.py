from fastapi.testclient import TestClient
from main import app


def test_get_all_products():
    client = TestClient(app)
    response = client.get("/product/all")
    assert response.status_code == 404
