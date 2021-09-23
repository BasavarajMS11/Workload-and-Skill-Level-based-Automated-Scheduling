from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from django.db import models
from import_export import resources


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class MonthForm(forms.ModelForm):
    class Meta:
        model = Months
        fields = ('name', 'workdays', 'workhours')

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machines
        fields = ('id','mcid','vsmname','mcname','mcskilllevel','nomcs','stdmng','opperhour','efficiency')

class MPPResource(forms.ModelForm):
    class Meta:
        model=MPP
        fields = ('vsmname','mcname','prodqty')      
'''class MPPResourceMar1(forms.ModelForm):
    class Meta:
        model=MPPMarch1s
        fields = ('vsmname','mcname','prodqty')

class MPPResourceMar2(forms.ModelForm):
    class Meta:
        model=MPPMarch2s
        fields = ('vsmname','mcname','prodqty')'''

class ManpowerForm(forms.ModelForm):
    class Meta:
        model=Manpowers
        fields = ('vsmname','mcname','prodqty','stdmng','nomcs','manpower','shifts')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model= Employees
        fields = ('id','empid','empname','doj','mcname','skilllevel')

class ScheduleForm(forms.ModelForm):
    class Meta:
        model=Schedules
        fields = ('vsmname','mcname','shiftnor','empid','empname','url')