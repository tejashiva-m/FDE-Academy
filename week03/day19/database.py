from __future__ import annotations

from collections.abc import Generator

import psycopg
from psycopg.rows import dict_row

from config import (
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USER,
)


def connect():
    return psycopg.connect(
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        row_factory=dict_row,
    )


def create_tables(connection) -> None:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                department TEXT NOT NULL,
                salary REAL NOT NULL CHECK (salary > 0)
            )
            """
        )
    connection.commit()


def get_db() -> Generator:
    connection = connect()
    create_tables(connection)
    try:
        yield connection
    finally:
        connection.close()
