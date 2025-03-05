from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from ecomapp.models import Contact,product


#from rest_framework import viewsets




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



def contact_view(request):
   

    context = {}

    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Save the contact data
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('contact') 

    # Fetch all contact data to display
    data = Contact.objects.all()
    context["contact"] = data

    return render(request, "Contact.html", context)

def details_oneplus(request):
    return render (request, "oneplus.html")

def details_samsung(request):
    return render (request, "samsung.html")

def details_realme(request):
    return render (request, "realme.html")

def details_apple(request):
    return render (request, "apple.html")

def details_vivo(request):
    return render (request, "vivo.html")

def details_oppo(request):
    return render (request, "oppo.html")

def product_view(request):
    context = {}

    if request.method == "POST":
        data = request.POST
        customer_name = data.get("customer_name")
        mobile = data.get("mobile")
        name = data.get('name')
        price = data.get('price')
        stock = data.get('stock')
        image = request.FILES.get('image')

        if name and price and stock:  # Ensure required fields are present
            product.objects.create(
                name=name,
                price=price,
                stock=stock,
                image=image,
                customer_name=customer_name,
                mobile=mobile
            )
            return redirect('product')  # Redirect to avoid resubmitting form

    # Fetch products
    data = product.objects.all()
    context["products"] = data

    return render(request, "buynow.html", context)


def paynow(request):
    return render (request, "paynow.html")


def products(request):
    return render (request, "products.html")

def index(request):
    return render (request, "index.html")





