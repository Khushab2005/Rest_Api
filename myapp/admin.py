from django.contrib import admin
from myapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'salary', 'date_of_birth', 'join_date', 'created_at', 'updated_at',)
    list_display_links = ('name','email')
    search_fields = ('name', 'email')
    list_per_page = 10
    list_filter = ('gender', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    


admin.site.register(Employee, EmployeeAdmin)


