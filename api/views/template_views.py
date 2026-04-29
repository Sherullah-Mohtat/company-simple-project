from django.shortcuts import render
from api.models import Company, Employee


def home(request):
    return render(request, "api/home.html")


def company_list(request):
    companies = Company.objects.all()
    return render(request, "api/company_list.html", {"companies": companies})


def employee_list(request):
    employees = Employee.objects.select_related("company").all()
    return render(request, "api/employee_list.html", {"employees": employees})