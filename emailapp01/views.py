from django.shortcuts import render
from .forms import EmployeeForm
from .signals import new_emp_create
from .models import Employee
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    form = EmployeeForm
    # print(form)

    if request.method == "POST":
        data = EmployeeForm(request.POST)       # fron end 
        if data.is_valid():
            Name = data.cleaned_data['Name']        # request.POST.get
            Surname = data.cleaned_data['Surname']
            Address = data.cleaned_data['Address']
            Email = data.cleaned_data['Email']
            
            data.save()

            new_emp_create.send(sender=Employee,Name=Name,Surname=Surname,Address=Address,Email=Email )
            
            return HttpResponse("Data Send Successfully")

    else:
        return render(request,"home.html",{"form":form})
