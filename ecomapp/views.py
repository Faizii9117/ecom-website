from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    

    return render(request, "index.html")


def auth_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")

    return render(request, "login.html")


def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("/login")
