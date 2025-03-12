from django.contrib import admin
from .models import Contact ,Order, Items,Register

# Register the Contact model
admin.site.register(Register)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(Items)

