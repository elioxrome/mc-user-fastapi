def test_create_user_success(client):
    payload = {"name": "Ana", "email": "ana@example.com"}

    response = client.post("/api/v1/users", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["id"]
    assert body["name"] == payload["name"]
    assert body["email"] == payload["email"]


def test_create_user_duplicate_email_returns_409(client):
    payload = {"name": "Ana", "email": "ana@example.com"}
    client.post("/api/v1/users", json=payload)

    response = client.post("/api/v1/users", json=payload)

    assert response.status_code == 409
    assert "ya existe" in response.json()["detail"]


def test_update_user_success(client):
    created = client.post(
        "/api/v1/users", json={"name": "Ana", "email": "ana@example.com"}
    ).json()

    response = client.put(
        f"/api/v1/users/{created['id']}",
        json={"name": "Ana Maria", "email": "ana.maria@example.com"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == created["id"]
    assert body["name"] == "Ana Maria"
    assert body["email"] == "ana.maria@example.com"


def test_update_user_not_found_returns_404(client):
    response = client.put(
        "/api/v1/users/not-found-id",
        json={"name": "Ana Maria", "email": "ana.maria@example.com"},
    )

    assert response.status_code == 404
    assert "no encontrado" in response.json()["detail"]


def test_update_user_with_duplicate_email_returns_409(client):
    first = client.post(
        "/api/v1/users", json={"name": "Ana", "email": "ana@example.com"}
    ).json()
    client.post("/api/v1/users", json={"name": "Luis", "email": "luis@example.com"})

    response = client.put(
        f"/api/v1/users/{first['id']}",
        json={"name": "Ana", "email": "luis@example.com"},
    )

    assert response.status_code == 409
    assert "ya existe" in response.json()["detail"]


def test_delete_user_success(client):
    created = client.post(
        "/api/v1/users", json={"name": "Ana", "email": "ana@example.com"}
    ).json()

    response = client.delete(f"/api/v1/users/{created['id']}")

    assert response.status_code == 204
    assert response.text == ""


def test_delete_user_not_found_returns_404(client):
    response = client.delete("/api/v1/users/not-found-id")

    assert response.status_code == 404
    assert "no encontrado" in response.json()["detail"]
