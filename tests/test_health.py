def test_health_endpoint_returns_up(client):
    response = client.get("/actuator/health")

    assert response.status_code == 200
    assert response.json() == {"status": "UP"}
