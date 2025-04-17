import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_index_products():
    response = client.get("/api/products")
    assert response.status_code == 200

def test_create_product():
    payload = {"name": "Test Product", "price": 123.45}
    response = client.post("/api/products", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 123.45

def test_get_product():
    # Сначала создаём продукт
    payload = {"name": "Get Product", "price": 10}
    create_resp = client.post("/api/products", json=payload)
    product_id = create_resp.json()["id"]

    # Получаем его по id
    response = client.get(f"/api/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Get Product"

def test_update_product():
    payload = {"name": "Old Name", "price": 1}
    create_resp = client.post("/api/products", json=payload)
    product_id = create_resp.json()["id"]

    update_payload = {"name": "New Name", "price": 2}
    response = client.put(f"/api/products/{product_id}", json=update_payload)
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"
    assert response.json()["price"] == 2

def test_delete_product():
    payload = {"name": "To Delete", "price": 5}
    create_resp = client.post("/api/products", json=payload)
    product_id = create_resp.json()["id"]

    response = client.delete(f"/api/products/{product_id}")
    assert response.status_code == 200

    get_resp = client.get(f"/api/products/{product_id}")
    assert get_resp.json() is None
