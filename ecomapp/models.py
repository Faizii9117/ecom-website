from django.db import models
# Create your models here.
class login ():
    username = models.CharField(max_length=20)
    password = models.IntegerField()
    

class register():
   username = models.CharField(max_length=20)
   password = models.IntegerField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

