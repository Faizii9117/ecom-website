from django.db import models
from colorfield.fields import ColorField


class Login(models.Model): 
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  
    def __str__(self):
        return self.username


class Register(models.Model):  # Fixed name and added models.Model
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=255)  # Changed from IntegerField to CharField

    def __str__(self):
        return self.username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name





class Items(models.Model):
    CONDITION_CHOICES = [
        ("New", "New"),
        ("Refurbished", "Refurbished"),
        ("Old", "Old"),
    ]
    item_name = models.CharField(max_length=50)
    item_heading = models.CharField(max_length=100)
    item_id = models.AutoField(primary_key=True)
    item_img = models.ImageField()
    item_desc = models.TextField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default="New")
    item_color = ColorField(default="#FFFFFF")
    is_damaged = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name


class Order(models.Model):  
    PAYMENT_CHOICES = [
        ("COD", "Cash on Delivery"),
        ("Online", "Online Payment"),
    ]
    customer_name = models.CharField(max_length=100)  # Increase this if necessary
    mobile_no = models.CharField(max_length=15)  # Increase from 12 to 15
    address = models.CharField(max_length=255)  # Ensure enough space for full address
    landmark = models.CharField(max_length=100, blank=True, null=True)
    payment_mode = models.CharField(max_length=20, choices=[("COD", "Cash on Delivery"), ("Online", "Online Payment")])

    def __str__(self):
        return self.customer_name
