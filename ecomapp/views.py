from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    

    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Call the save method
            auth_login(request, user)  # Log the user in
            return redirect('/login')  # Redirect to a success page or home
            
    else:
        initial_data = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)
    
    return render(request, 'register.html', {'form': form})   



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


def contact(request):
    return render (request, "contact.html")