from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="product/", null=True, blank=True)
    customer_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    


    def __str__(self):
        return self.name


class login(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)


    def __str__(self):
        return self.username
    














'''class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.models.CharField(max_length=50)



    def __str__(self):
        return self.username'''