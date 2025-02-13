from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'home_page.html')

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
                return redirect('passenger_dashboard')
        else:
            messages.error(request, "There was an error logging in, try again...")
            return render(request, 'login_page.html')
    return render(request, "login_page.html")

def is_admin(user):
    return user.is_authenticated and user.role=="admin"

def is_passenger(user):
    return user.is_authenticated and user.role=="passenger"

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

@login_required
@user_passes_test(is_passenger)
def passenger_dashboard(request):
    return render(request, "home_page.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('home')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, "registration_page.html", {"form": form})

