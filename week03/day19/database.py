from __future__ import annotations

import os
import sqlite3
from collections.abc import Generator
from pathlib import Path


DATABASE_PATH = Path(
    os.getenv("DATABASE_PATH", Path(__file__).with_name("employees.db"))
)


def connect(path: str | Path = DATABASE_PATH) -> sqlite3.Connection:
    connection = sqlite3.connect(path, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            department TEXT NOT NULL,
            salary REAL NOT NULL CHECK (salary > 0)
        )
        """
    )
    connection.commit()


def get_db() -> Generator[sqlite3.Connection, None, None]:
    connection = connect()
    create_tables(connection)
    try:
        yield connection
    finally:
        connection.close()
