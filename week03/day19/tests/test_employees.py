import pytest
from database import connect, create_tables, get_db
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client(tmp_path):
    database_path = tmp_path / "test_employees.db"

    def override_get_db():
        connection = connect(database_path)
        create_tables(connection)
        try:
            yield connection
        finally:
            connection.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def employee_payload():
    return {
        "name": "Maya Patel",
        "email": "maya.patel@example.com",
        "department": "Platform Engineering",
        "salary": 125000,
    }


def create_employee(client, employee_payload):
    response = client.post("/employees", json=employee_payload)
    assert response.status_code == 201
    return response.json()


def test_create_employee(client, employee_payload):
    employee = create_employee(client, employee_payload)

    assert employee["id"] == 1
    assert employee["name"] == "Maya Patel"
    assert employee["email"] == "maya.patel@example.com"


def test_list_employees(client, employee_payload):
    created = create_employee(client, employee_payload)

    response = client.get("/employees")

    assert response.status_code == 200
    assert response.json() == [created]


def test_list_employees_returns_empty_list(client):
    response = client.get("/employees")

    assert response.status_code == 200
    assert response.json() == []


def test_get_employee_by_id(client, employee_payload):
    created = create_employee(client, employee_payload)

    response = client.get(f"/employees/{created['id']}")

    assert response.status_code == 200
    assert response.json() == created


def test_update_employee(client, employee_payload):
    created = create_employee(client, employee_payload)
    updated_payload = {
        **employee_payload,
        "department": "Site Reliability Engineering",
        "salary": 132000,
    }

    response = client.put(f"/employees/{created['id']}", json=updated_payload)

    assert response.status_code == 200
    assert response.json()["department"] == "Site Reliability Engineering"
    assert response.json()["salary"] == 132000


def test_delete_employee(client, employee_payload):
    created = create_employee(client, employee_payload)

    response = client.delete(f"/employees/{created['id']}")

    assert response.status_code == 204
    assert response.content == b""
    assert client.get(f"/employees/{created['id']}").status_code == 404


@pytest.mark.parametrize("method", ["get", "put", "delete"])
def test_missing_employee_returns_404(client, employee_payload, method):
    if method == "put":
        response = client.put("/employees/999", json=employee_payload)
    else:
        response = getattr(client, method)("/employees/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee not found"}


@pytest.mark.parametrize(
    "invalid_field,invalid_value",
    [
        ("name", ""),
        ("email", "not-an-email"),
        ("department", ""),
        ("salary", 0),
        ("salary", -100),
    ],
)
def test_create_employee_validation_failure(
    client, employee_payload, invalid_field, invalid_value
):
    invalid_payload = {**employee_payload, invalid_field: invalid_value}

    response = client.post("/employees", json=invalid_payload)

    assert response.status_code == 422


def test_update_employee_validation_failure(client, employee_payload):
    created = create_employee(client, employee_payload)
    invalid_payload = {**employee_payload, "email": "invalid"}

    response = client.put(f"/employees/{created['id']}", json=invalid_payload)

    assert response.status_code == 422


def test_duplicate_email_returns_409(client, employee_payload):
    create_employee(client, employee_payload)
    duplicate_payload = {**employee_payload, "name": "Another Employee"}

    response = client.post("/employees", json=duplicate_payload)

    assert response.status_code == 409
    assert response.json() == {
        "detail": "An employee with this email already exists"
    }


def test_update_to_duplicate_email_returns_409(client, employee_payload):
    create_employee(client, employee_payload)
    second_payload = {
        **employee_payload,
        "name": "Noah Williams",
        "email": "noah.williams@example.com",
    }
    second = create_employee(client, second_payload)
    conflicting_payload = {**second_payload, "email": employee_payload["email"]}

    response = client.put(
        f"/employees/{second['id']}", json=conflicting_payload
    )

    assert response.status_code == 409
