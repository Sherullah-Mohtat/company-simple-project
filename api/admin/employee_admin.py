from django.contrib import admin
from api.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','company')
    list_filter = ('company',)

admin.site.register(Employee, EmployeeAdmin)
