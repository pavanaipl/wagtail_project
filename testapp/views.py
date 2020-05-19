from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import *
from django.shortcuts import render, get_object_or_404


# Create your views here.
def testing(request):
    page = {
        "title":"Bob details",
        "name":"bob",
        "age":45,
        "mobile_number":"78738389323",
        "email":"bob@gmail.com"
    }
    return render(request, 'testapp/users_details.html', {"page":page})




def create_employee(request):
    if request.method == "POST":
        form = FormPage(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('employee_details', pk=post.pk)
    else:
        form = FormPage()
    return render(request, 'testapp/create_employee.html', {'form': form})

def employee_detail(request, pk):
    post = get_object_or_404(EmployeeDetails, pk=pk)
    return render(request, 'testapp/employee_detail.html', {'post': post})



def suggest(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            flavour = form.save()
            return render(request, 'testapp/thankyou.html', {
                'flavour': flavour,
            })
    else:
        form = EmployeeForm()
    return render(request, 'testapp/suggest.html', {
        'form': form,
    })