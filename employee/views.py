from django.shortcuts import render, redirect
from employee.models import Employee
from employee.forms import EmployeeForm
# Create your views here.

# REVIEW: this is add method
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'employee/index.html', { 'form' : form })

def show(request):
    employees = Employee.objects
    return render(request,'employee/show.html', { 'employees' : employees })

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employee/edit.html', { 'employee' : employee } )

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        try:
            form.save()
            return redirect('/show')
        except:
            pass
    return render(request, 'employee/edit.html', { 'employee' : employee })

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')