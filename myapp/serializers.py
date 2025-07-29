from rest_framework import serializers
from myapp.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'gender','salary', 'date_of_birth', 'join_date' ]
        read_only_fields = ('created_at',)
        write_only_fields = ('updated_at',)
        
