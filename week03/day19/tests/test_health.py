from unittest.mock import patch

import psycopg
import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_liveness_check(client):
    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {
        "status": "alive"
    }


def test_readiness_check(client):
    response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready",
        "database": "connected",
    }


@patch("health.connect")
def test_readiness_check_database_unavailable(mock_connect, client):
    mock_connect.side_effect = psycopg.OperationalError(
        "Database connection failed"
    )

    response = client.get("/health/ready")

    assert response.status_code == 503
    assert response.json() == {
        "detail": {
            "status": "not ready",
            "database": "unavailable",
        }
    }