from django.shortcuts import render, redirect



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

