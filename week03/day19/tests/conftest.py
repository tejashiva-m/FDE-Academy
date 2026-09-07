import pytest
from fastapi.testclient import TestClient

from database import connect, create_tables, get_db
from main import app


@pytest.fixture
def db_connection():
    connection = connect()
    create_tables(connection)

    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE employees RESTART IDENTITY")

    connection.commit()

    yield connection

    connection.close()


@pytest.fixture
def client(db_connection):
    def override_get_db():
        yield db_connection

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()