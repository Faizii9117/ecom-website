from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from ecomapp.models import Contact
from .serializers import userserializer
from ecomapp.models import *
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect
from twilio.rest import Client
from .models import Order  




#from rest_framework import viewsets




def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    item_data = Items.objects.all()

    return render(request, "index.html", {'item_data': item_data})

def register(request):
    if request.method == "POST":
        form = userserializer(request.POST)
        if form.is_valid():
            user = form.save()  # Call the save method
            auth_login(request, user)  # Log the user in
            return redirect('/login')  # Redirect to a success page or home
            
    else:
        initial_data = {'username':'','password1':'','password2':''}
        form = userserializer(initial=initial_data)
    
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

        return redirect('index') 
 
    # Fetch all contact data to display
    data = Contact.objects.all()
    context["contact"] = data

    return render(request, "Contact.html", context)





def item(request):
    if request.method == "POST":
        data = request.POST
        item_name = data.get("item_name")
        item_heading = data.get("item_heading")
        item_desc = data.get("item_desc") 
        item_img = request.FILES.get("item_img")
        item_condition=data.get('item_condition')
        item_price = data.get("item_price")
        item_color=data.get("item_color")
        is_damaged = data.get("is_damaged") == "on"

        Items.objects.create(
            item_name=item_name,
            item_heading=item_heading,
            item_desc=item_desc,
            item_img=item_img,
            item_condition=item_condition, 
            item_price=item_price,
            item_color=item_color,
            is_damaged=is_damaged,
        )
        return redirect("index")  

    
    data = Items.objects.all()
    context = {"item_data": data}

    return render(request, "items.html", context)


def delete_product(request, id):
    queryset=Items.objects.get(item_id=id)
    queryset.delete()
    return redirect('index')


def product_detail(request, id):
    detail = get_object_or_404(Items, item_id=id) 
    return render(request, 'product_detail.html', {'detail': detail})


# def product_detail_1(request, id):
#     detail_1 = get_object_or_404(Items, item_id=id) 
#     return render(request, 'product_detail_1.html', {'detail_1': detail_1})








def buy_now(request,id):
    product_ordered = get_object_or_404(Items, item_id=id)     
    if request.method == "POST":
        print("🛒 buy_now view called!")  # Ensure this prints

        customer_name = request.POST.get("customer_name")
        mobile_no = request.POST.get("mobile_no")
        address = request.POST.get("address")
        landmark = request.POST.get("landmark")
        payment_mode = request.POST.get("payment_mode")

        print(f"📢 Data received: {customer_name}, {mobile_no}, {address}, {landmark}, {payment_mode}") 
        order = Order.objects.create(
            customer_name=customer_name,
            mobile_no=mobile_no,
            address=address,
            landmark=landmark,
            payment_mode=payment_mode,
            )
        print(f"✅ Order created: {order}")  # Debugging
        return redirect("/")
    
    data = Order.objects.all()
    context = {
        "order_data": data,
        "ordered_product": product_ordered
         }
    return render(request, "buynow.html",context)
