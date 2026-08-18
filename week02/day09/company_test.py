from company.employee import Employee
from company.intern import Intern
from company.manager import Manager

employee = Employee("Teja", "Cloud", 120000)
manager = Manager("Alice", "Cloud", 150000, 8)
intern = Intern("Bob", "Cloud", 30000, "UT Dallas")

employee.display()
manager.display()
intern.display()