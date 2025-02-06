from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


def home(request):
    return render('./templates/home_page.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, "There was an error logging in, try again...")
    return render(request, 'login_view.html')

def is_admin(user):
    return user.is_authenticated and user.role=="admin"

def is_passeneger(user):
    return user.is_authenticated and user.role=="passenger"

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

@login_required
@user_passes_test(is_passeneger)
def home_page(request):
    return render(request, "home_page.html")

