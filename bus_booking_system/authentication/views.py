from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def home(request):
    return render('./templates/home_page.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page.html')
        else:
            messages.error(request, "There was an error logging in, try again...")
            return render(request, 'login_page.html')
    else:
        return render(request, "login_page.html")