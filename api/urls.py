from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers
from api.views.template_views import home, company_list, employee_list

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
urlpatterns = [
    path('', include(router.urls)),

    path("pages/", home, name="home"),
    path("pages/companies/", company_list, name="company-list-page"),
    path("pages/employees/", employee_list, name="employee-list-page"),
]
