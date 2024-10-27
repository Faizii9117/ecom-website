from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Call the save method
            auth_login(request, user)  # Log the user in
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('/')  # Redirect to the home page
            
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def auth_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html", {"username": username})

    return render(request, "login.html")

def logout_view(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("/login")

def contact(request):
    return render(request, "contact.html")

def details_oneplus(request):
    return render(request, "oneplus.html")

def details_samsung(request):
    return render(request, "samsung.html")

def details_realme(request):
    return render(request, "realme.html")

def details_apple(request):
    return render(request, "apple.html")

def details_vivo(request):
    return render(request, "vivo.html")

def details_oppo(request):
    return render(request, "oppo.html")
