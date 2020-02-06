# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:11:28 2020

@author: C803659
"""

from django import forms
from employee.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"