from django.db import models
from django.core import validators
from django.core.validators import *
# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sid=models.IntegerField()
    phone=models.CharField(max_length=10,validators=[validators.RegexValidator(r'[6-9]\d{9}')])
    
    
    def __str__(self):
        return self.sname