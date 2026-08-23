import os


DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = int(os.getenv("DATABASE_PORT", "5432"))
DATABASE_NAME = os.getenv("DATABASE_NAME", "employees")
DATABASE_USER = os.getenv("DATABASE_USER", "employee_user")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "employee_password")