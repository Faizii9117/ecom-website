from django.contrib import admin
from .models import Contact ,product # Import the Contact model

# Register the Contact model
admin.site.register(Contact)
admin.site.register(product)
