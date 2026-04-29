from django.test import TestCase
from api.models import Company

class CompanyModelTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Tech Company",
            location="California",
            about="Software company",
            type="IT",
            active=True
        )

    def test_company_created_successfully(self):
        self.assertEqual(self.company.name, "Tech Company")
        self.assertEqual(self.company.location, "California")
        self.assertTrue(self.company.active)

    def test_company_string_method(self):
        self.assertEqual(str(self.company), "Tech Company California")