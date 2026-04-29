from django.test import TestCase
from api.models import Company, Employee

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name="Tech Company",
            location="California",
            about="Software company",
            type="IT",
            active=True
        )

        self.employee = Employee.objects.create(
            name="Sherullah Mohtat",
            email="sherullah@example.com",
            address="Sacramento",
            phone="1234567890",
            position="Software Developer",
            company=self.company
        )

    def test_employee_created_successfully(self):
        self.assertEqual(self.employee.name, "Sherullah Mohtat")
        self.assertEqual(self.employee.email, "sherullah@example.com")
        self.assertEqual(self.employee.company, self.company)

    def test_employee_string_method(self):
        self.assertEqual(str(self.employee), "Sherullah Mohtat")

    def test_employee_company_relationship(self):
        self.assertEqual(self.employee.company.name, "Tech Company")