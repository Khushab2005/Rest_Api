from django.db import models
from myapp.constants import GENDER_CHOICES
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(blank=False, null=False,unique=True)
    gender = models.CharField(max_length=50, blank=False, null=False ,choices=GENDER_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    join_date = models.DateField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    