import sqlite3
from pathlib import Path


class Database:
    def __init__(self, db_path="company.db"):
        default_path = Path(__file__).resolve().parent / "company.db"
        if db_path is None:
            self.db_path = default_path
        else:
            self.db_path = Path(db_path)
            if not self.db_path.is_absolute():
                self.db_path = Path(__file__).resolve().parent / self.db_path
        self.connection = sqlite3.connect(str(self.db_path))
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self._initialize_schema()

    def _initialize_schema(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary INTEGER NOT NULL
            )
            """
        )
        self.connection.commit()

    def close(self):
        self.connection.close()

    def execute(self, query, params=()):
        return self.cursor.execute(query, params)

    def commit(self):
        self.connection.commit()
