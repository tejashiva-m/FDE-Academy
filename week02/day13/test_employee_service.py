import os
import sys
import tempfile
import unittest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

try:
    from week02.day13.employee_service import EmployeeService
except ModuleNotFoundError:
    from employee_service import EmployeeService


class EmployeeServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_company.db")
        self.service = EmployeeService(self.db_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_crud_and_reports(self):
        self.service.create_employee("Asha", "Engineering", 90000)
        self.service.create_employee("Ben", "Sales", 80000)
        self.service.create_employee("Cara", "Engineering", 95000)

        employees = self.service.list_employees()
        self.assertEqual(3, len(employees))

        found = self.service.search_by_name("Asha")
        self.assertEqual("Asha", found[0].name)

        self.service.update_salary(1, 100000)
        updated = self.service.get_employee(1)
        self.assertEqual(100000, updated.salary)

        self.service.delete_employee(2)
        remaining = self.service.list_employees()
        self.assertEqual(2, len(remaining))

        self.assertEqual(97500.0, self.service.get_average_salary())
        self.assertEqual(100000, self.service.get_highest_salary())
        self.assertEqual(2, self.service.count_by_department("Engineering"))

        sorted_employees = self.service.list_employees_sorted_by_salary()
        self.assertEqual(["Asha", "Cara"], [e.name for e in sorted_employees])


if __name__ == "__main__":
    unittest.main()
