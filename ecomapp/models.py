from django.db import models

# Create your models here.
class login ():
    username = models.CharField(max_length=20)
    password = models.IntegerField()
    

class register():
   username = models.CharField(max_length=20)
   password = models.IntegerField()
