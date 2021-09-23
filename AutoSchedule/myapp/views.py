from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Months, usersLog
from datetime import datetime
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from tablib import Dataset
from django.http import HttpResponse
from io import TextIOWrapper
import csv
import pandas as pd
from django.contrib.auth.decorators import login_required
import math


# Create your views here.
'''def index(request): 
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')


    return render(request,'login.html') '''

def yetto(request):
    if request.method=='POST':
        vsm=request.POST.get('vsm')
        items = Manpowers.objects.filter(vsmname=vsm)
        Schedules.objects.all().delete()
        print(items.values_list)
        nor=0
        for item in items:
            pershiftmp=item.manpower//item.shifts
            emps= Employees.objects.filter(mcname=item.mcname).filter(skilllevel__gte=item.skilllevel)
            #print(emps.values_list)
            #print(emps.values_list)
            for shift in range(item.shifts):
                for per in range(pershiftmp):
                    print(emps[nor])
                    vsmname=vsm
                    mcname=item.mcname
                    shiftnor=shift+1
                    empid=emps[nor].empid
                    empname=emps[nor].empname
                    url="https://www.kindpng.com/picc/m/78-785975_icon-profile-bio-avatar-person-symbol-chat-icon.png"
                    if Schedules.objects.filter(empid=emps[nor].empid).exists():
                        nor+=1
                        empid=emps[nor].empid
                        empname=emps[nor].empname
                    value=Schedules.objects.create(vsmname=vsmname,mcname=mcname,shiftnor=shiftnor,empid=empid,empname=empname, url=url)
                    value.save()
                    nor+=1

                    #print(items.values_list)
                    #print(vsm)

        #vsm=request.POST.get('vsm')
        items = Schedules.objects.filter(vsmname=vsm)
        context = {
            'items': items,
            'header': 'Schedules',
        }
        return render(request, 'crud/yetto.html', context)

        #password=request.POST.get('password')
    return render(request, 'crud/yetto.html')

'''def schedule_display(request):
    if request.method=='POST':
        vsm=request.POST.get('vsm')
        items = Schedules.objects.filter(vsmname=vsm)
        context = {
            'items': items,
            'header': 'Schedules',
        }
    
    return render(request, 'crud/yetto.html', context)'''

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/home2') 
        else:
            messages.info(request,'Username or Password Incorrect')
    return render(request,'logintemp/login.html') 


def logoutUser(request):
    logout(request)
    return redirect('/login')

#@login_required(login_url='login')
def home(request):
    return render(request,'logintemp/home.html')

@login_required(login_url='login')
def home2(request):
    return render(request,'logintemp/home2.html')


def registration(request):
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account Created Successfully for '+user)
            return redirect('/login')

    context={'form':form}
    return render(request,'logintemp/registration.html',context)
    

def menu(request):
    return render(request,'logintemp/page2.html')

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home2')

    else:
        form = cls()
        return render(request, 'crud/add_item.html', {'form' : form})

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home2')
    else:
        form = cls(instance=item)

        return render(request, 'crud/edit_item.html', {'form': form})

'''def edit_mpp(request, pk):
    return edit_item(request, pk, MPPs, MPPResource)'''

def mpp(request):
    return render(request,'monthlyplan/monthlyplan.html')

def mppupload(request):
    return render(request,'monthlyplan/monthlyplanupload.html')

def mppprevious(request):
    return render(request,'monthlyplan/monthlyplanprevious.html')

def monthlypp(request):
    '''if request.method=="POST":
        form=MPPResource()
        new_file=request.FILES['csvfile']
        with open(new_file,'r') as f:
            reader=csv.reader(f)
            df=pd.read_csv(f)
            dictdata=df.to_dict('records')
            value=MPP(dictdata)
            value.save()
    return render(request,'page6.html')'''

    if request.method=="POST":
        #month_prod_plan=MPPResource()
        month=request.POST.get('month')
        version=request.POST.get('version')
        dataset=Dataset()
        #new_file=request.FILES['csvfile']
        new_file= TextIOWrapper(request.FILES['csvfile'].file)

        '''if not new_file.name.endswith('csv'):
            messages.info(request,'Wrong Format')
            return render(request,'page5.html')'''

        imported_data = dataset.load(new_file.read(),format='csv')
        
        for data in imported_data:
            if(month=="Mar" and version=="Version 1"):
                value = MPPMarch1s(
                data[0],
                data[1],
                data[2],
                data[3]
                )
                value.save()
                items = MPPMarch1s.objects.all()
                context = {
                'items': items,
                'header': 'MPMarch1Ps',
                }
            if(month=="Mar" and version=="Version 2"):
                value = MPPMarch2s(
                data[0],
                data[1],
                data[2],
                data[3]
                )
                value.save()
                items = MPPMarch2s.objects.all()
                context = {
                'items': items,
                'header': 'MPPMarch2s',
                }

        return render(request, 'crud/mppindex.html', context)
'''
def mppindex(request):
    return render(request, 'crud/mppindex.html')

'''


#@login_required(login_url='login')
def display_mpps(request):
    if request.method=="POST":
        month=request.POST.get('month')
        version=request.POST.get('version')

        if(month=="Mar" and version=="Version 1"):
            items = MPPMarch1s.objects.all()
            context = {
            'month':'Mar',
            'version':'Version 1',
            'items': items,
            'header': 'MPPMarch1s',
            }
            return render(request, 'crud/mppindex.html', context)
        if(month=="Mar" and version=="Version 2"):
            items = MPPMarch2s.objects.all()
            context = {
            'month':'Mar',
            'version':'Version 2',
            'items': items,
            'header': 'MPPMarch2s',
            }
            return render(request, 'crud/mppindex.html', context)

    

def add_mpp(request):
    return add_item(request, MPPResource)

def edit_mpp(request, month,version,pk):
    if(month=="Mar" and version=="Version 1"):
        items = MPPMarch1s
        resources= MPPResource
    if(month=="Mar" and version=="Version 2"):
        items = MPPMarch2s
        resources= MPPResource
        
    return edit_item(request, pk, items, resources)

def delete_mpp(request, pk):
    
    template = 'crud/mppindex.html'
    MPP.objects.filter(id=pk).delete()

    items = MPP.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
    
def machine(request):
    return redirect('/display_machines')

def emp(request):
    return redirect('/display_employees')

def month(request):
    return redirect('/display_months')

def about(request):
    return render(request,'logintemp/about.html')

@login_required(login_url='/login')
def index(request):
    return render(request, 'crud/index.html')

@login_required(login_url='/login')
def display_months(request):
    items = Months.objects.all()
    context = {
        'items': items,
        'header': 'Months',
    }
    return render(request, 'crud/index.html', context)


def add_month(request):
    return add_item(request, MonthForm)


def edit_month(request, pk):
    return edit_item(request, pk, Months, MonthForm)

def delete_month(request, pk):
    
    template = 'crud/index.html'
    Months.objects.filter(id=pk).delete()

    items = Months.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def machineindex(request):
    return render(request, 'crud/machineindex.html')

@login_required(login_url='login')
def display_machines(request):
    items = Machines.objects.all()
    context = {
        'items': items,
        'header': 'Machines',
    }
    return render(request, 'crud/machineindex.html', context)


def add_machine(request):
    return add_item(request, MachineForm)

def edit_machine(request, pk):
    return edit_item(request, pk, Machines, MachineForm)

def delete_machine(request, pk):
    
    template = 'crud/machineindex.html'
    Machines.objects.filter(id=pk).delete()

    items = Machines.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def employeeindex(request):
    return render(request, 'crud/employeeindex.html')

@login_required(login_url='login')
def display_employees(request):
    items = Employees.objects.all()
    context = {
        'items': items,
        'header': 'Employees',
    }
    return render(request, 'crud/employeeindex.html', context)


def add_employee(request):
    return add_item(request, EmployeeForm)

def edit_employee(request, pk):
    return edit_item(request, pk, Employees, EmployeeForm)

def delete_employee(request, pk):
    
    template = 'crud/employeeindex.html'
    Employees.objects.filter(id=pk).delete()

    items = Employees.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def manpower_calculation(request):
    plans = MPP.objects.all()
    mcdetails = Machines.objects.all()
    Manpowers.objects.all().delete()
    form=ManpowerForm()
    '''for plan in plans:
        form.'''

    for plan in plans.iterator():
        for detail in mcdetails.iterator():
            if plan.mcname==detail.mcname:
                vsmname=plan.vsmname
                mcname=plan.mcname
                skilllevel=detail.mcskilllevel
                prodqty=plan.prodqty
                stdmng=detail.stdmng
                nomcs=detail.nomcs
                capacity=detail.opperhour*20.6*27*1*0.85
                mp=detail.stdmng*3*plan.prodqty
                mp=mp/capacity
                shifts=mp/math.ceil(detail.stdmng)
                #('id','vsmname','mcname','prodqty','stdmng','nomcs','manpower','shifts'
                value=Manpowers.objects.create(vsmname=vsmname,mcname=mcname,skilllevel=skilllevel,prodqty=prodqty,stdmng=stdmng, nomcs=nomcs, manpower=mp, shifts=shifts)
                value.save()


def manpower_display(request):
    manpower_calculation(request)
    items = Manpowers.objects.all()
    context = {
        'items': items,
        'header': 'Manpowers',
    }
    return render(request, 'crud/manpower.html', context)

def shift_display(request):
    #manpower_calculation(request)
    items = Manpowers.objects.all()
    context = {
        'items': items,
        'header': 'Manpowers',
    }
    return render(request, 'crud/shifts.html', context)


