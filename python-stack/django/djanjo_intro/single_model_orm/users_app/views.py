from django.shortcuts import render, redirect
from .models import User

# Route to display all users and the form
def index(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})

# Route to process the form submission
def add_user(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age
        )
        return redirect("/")  # redirect to main page
    return redirect("/")  # redirect if GET request
