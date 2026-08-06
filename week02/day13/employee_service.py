try:
    from .database import Database
    from .models import Employee
except ImportError:  # pragma: no cover - allows running the module directly
    from database import Database
    from models import Employee


class EmployeeService:
    def __init__(self, db_path="company.db"):
        self.db = Database(db_path)

    def create_employee(self, name, department, salary):
        self.db.execute(
            "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
            (name, department, salary),
        )
        self.db.commit()
        return self.db.cursor.lastrowid

    def get_employee(self, employee_id):
        row = self.db.execute("SELECT id, name, department, salary FROM employees WHERE id = ?", (employee_id,)).fetchone()
        if row is None:
            return None
        return Employee(row[0], row[1], row[2], row[3])

    def list_employees(self):
        rows = self.db.execute("SELECT id, name, department, salary FROM employees ORDER BY id").fetchall()
        return [Employee(row[0], row[1], row[2], row[3]) for row in rows]

    def search_by_name(self, name):
        rows = self.db.execute(
            "SELECT id, name, department, salary FROM employees WHERE name LIKE ? ORDER BY id",
            (f"%{name}%",),
        ).fetchall()
        return [Employee(row[0], row[1], row[2], row[3]) for row in rows]

    def search_by_department(self, department):
        rows = self.db.execute(
            "SELECT id, name, department, salary FROM employees WHERE department LIKE ? ORDER BY id",
            (f"%{department}%",),
        ).fetchall()
        return [Employee(row[0], row[1], row[2], row[3]) for row in rows]

    def list_employees_sorted_by_salary(self):
        rows = self.db.execute(
            "SELECT id, name, department, salary FROM employees ORDER BY salary DESC, id ASC"
        ).fetchall()
        return [Employee(row[0], row[1], row[2], row[3]) for row in rows]

    def get_average_salary(self):
        row = self.db.execute("SELECT AVG(salary) AS average_salary FROM employees").fetchone()
        return round(row[0], 2) if row[0] is not None else 0

    def get_highest_salary(self):
        row = self.db.execute("SELECT MAX(salary) AS highest_salary FROM employees").fetchone()
        return row[0] if row[0] is not None else 0

    def count_by_department(self, department):
        row = self.db.execute(
            "SELECT COUNT(*) AS total FROM employees WHERE department = ?",
            (department,),
        ).fetchone()
        return row[0]

    def update_salary(self, employee_id, new_salary):
        self.db.execute("UPDATE employees SET salary = ? WHERE id = ?", (new_salary, employee_id))
        self.db.commit()

    def delete_employee(self, employee_id):
        self.db.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
        self.db.commit()

    def close(self):
        self.db.close()
